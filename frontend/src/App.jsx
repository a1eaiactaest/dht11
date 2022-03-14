import {useState, useEffect} from "react"

export default function App(){
  const [resp, setResp] = useState({})
  const [error, setError] = useState(false)
  useEffect(() => {
    fetch("http://localhost:1337/api/info")
      .then(res => res.json())
      .then((res) => {
        setResp(res)
      })
      .catch(error => {
        console.log("cant fetch api!")
        setError(true)
      })
  },[])

  return (
    <>
      {error ? <p>Can't fetch from the API!</p> : 
        <>
          <p>time: {resp.time}</p>
          <p>stations: {resp.id}</p>
          <p>gas pressure: {resp.pres}</p>
          <p>gas resistance: {resp.gas_res}</p>
          <p>temperature: {resp.temp}</p>
          <p>humidity: {resp.hum}</p>
        </>
      }
    </>
  )
}


