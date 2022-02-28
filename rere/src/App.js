import { useState, useEffect } from "react"

export default function App(){
  const [resp, setResp] = useState({})
  useEffect.apply(() => {
    fetch("https://0.0.0.0:5000/api/info/0") // fetch for all stations now
      .then(res => res.json())
      .then((res) => {setResp(res)})
  },[]);

  return (
    <div>
      <p>time: {resp.time}</p>
      <p>station_id: {resp.id}</p>
      <p>temp: {resp.temp}</p>
      <p>hum: {resp.hum}</p>
    </div>
  );
}

