import { useState, useEffect } from "react";

import Homepage from "./homepage/Homepage";

import "./index.css";

function App(){

  const [resp, setResp] = useState({});
  const [error, setError] = useState(false);

  useEffect(() => {
    fetch("http://localhost:1337/api/serial_data?rows=1")
      .then(res => res.json())
      .then((res) => {
        console.log(res)
        setResp(res)
      })
      .catch(error => {
        console.log("cant fetch api!")
        setError(true)
      })
  },[]);

  return (
    <>
      {error ? <p>Can't fetch from the API!</p> : 
        <>
          <p>time: {resp.time}</p>
          <p>stations: {resp.id}</p>
          <p>gas pressure: {resp.air_pres}</p>
          <p>voc: {resp.voc}</p>
          <p>air temperature: {resp.air_temp}</p>
          <p>air humidity: {resp.air_hum}</p>
          <p>soil temperature: {resp.gnd_temp}</p>
          <p>soil humidity: {resp.gnd_hum}</p>
        </>
      }
      <Homepage />
    </>
  );
};

export default App;
