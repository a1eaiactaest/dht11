import { useState, useEffect } from "react";
import { Link } from "react-router-dom";

import Header from "../shared/components/Header";

function StationList(props) {
  const stations = props.stations;

  const listStations = stations?.map((station) => 
      <li key={station}>
        <Link to={`/stations/${station}`}>
          Station <b>{station}</b>
        </Link>
      </li>
  );

  return(
    <ul>
      <li key={0}><Link to={'/stations/0'}>All Stations</Link></li>
      {listStations}
    </ul>
  );
};

function Stations() {
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
    <main>
      <Header styleName="text-7xl" label="Stations"/>
      <StationList stations={stations} />
    </main>
  );
};

export default Stations;