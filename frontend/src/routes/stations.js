import { useState, useEffect } from "react";
import { Link } from "react-router-dom";

import Hero from "../shared/components/Hero";
import Menu from "../shared/components/Menu";

const StationList = (props) => {
  const stations = props.stations;

  const listStations = stations?.map((station) => 
      <a key={station} href={`/stations/${station}`} className="rounded-lg px-5 py-2 text-slate-900 font-medium hover:bg-slate-900 hover:text-green-400">
        Station <b>{station}</b>
      </a>
  );

  return(
    <nav className="flex sm:justify-center space-x-10">
      <a key={0} href={'/stations/0'} className="rounded-lg px-5 py-2 text-slate-900 font-medium hover:bg-slate-900 hover:text-green-400">
        All Stations
      </a>
      {listStations}
    </nav>
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
    </>
  );
};

export default Stations;