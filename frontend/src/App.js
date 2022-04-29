import { useState, useEffect } from "react";

import Homepage from "./homepage/Homepage";

import "./index.css";

function App(){

  /*
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
  */

  return (
    <>
      <Homepage />
    </>
  );
};

export default App;
