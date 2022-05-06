import { useState, useEffect } from "react";
import { Link } from "react-router-dom";

import Hero from "../shared/components/Hero";
import Menu from "../shared/components/Menu";

const StationList = (props) => {
  const stations = props.stations;

  const listStations = stations?.map((station) => 
      <li key={station}>
        <Link to={`/stations/${station}`}>
          Station <b>{station}</b>
        </Link>
      </li>
  );

  return(
    <ul className="flex sm:just space-x-4">
      <li key={0}><Link to={'/stations/0'}>All Stations</Link></li>
      {listStations}
    </ul>
  );
};

const Stations = () => {
  const [stations, setStations] = useState();

  useEffect(() => {
    fetch("http://localhost:1337/api/stations_index") 
      .then(res => res.json())
      .then((res) => {
        setStations(res)
      })
      .catch(error => {
        console.log('Request to http://localhost:1337/api/stations_index failed.')
      })
  }, []);

  return(
    <>
      <Hero header="Stations"/>
      <StationList stations={stations} />
      <br />
      <Menu elements={["test", "test1"]}/>
    </>
  );
};

export default Stations;