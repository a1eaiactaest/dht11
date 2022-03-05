import {useState, useEffect} from "react"

export default function App(){
  const [resp, setResp] = useState({})
  useEffect(() => {
    fetch("http://127:0.0.1:1337/api/info")
      .then(res => res.json())
      .then((res) => {
        setResp(res)
      })
      .catch(error => {
        console.log("cant fetch api!")
        return (
          <>
            <p>Can't fetch from the API!</p>
          </>
        )
      })
  },[])

  return (
    <>
      <p>time: {resp.time}</p>
      <p>stations: {resp.id}</p>
      <p>temperature: {resp.temp}</p>
      <p>humidity: {resp.hum}</p>
      <p>gas: {resp.gas}</p>
    </>
  )
}


