import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import Header from "../shared/components/Header";

import StationHomepage from "../station_homepage/StationHomepage";

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

  console.log(stations);
  return(
    <main>
      <Header className="text-3xl font-bold " label="Stations"/>
      <StationList stations={stations} />
    </main>
  );
};

export default Stations;