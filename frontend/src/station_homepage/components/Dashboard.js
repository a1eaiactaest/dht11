import React, { useEffect, useState } from 'react';

//import { extractDictItems } from "../../shared/utils/Array";
import MyChart from "../../shared/components/Charts";

function Dashboard(){
  // dummy
  const data_frame = [
    {
      name: 'a',
      air_temp: 16,
    },
    {
      air_temp: 17,
    },
    {
      'air_temp': 18,
    },
    {
      'air_temp': 15,
    },
    {
      'air_temp': 12,
    },
  ];

  const [data, setData] = useState([]);
  const [error, setError] = useState(false);

  useEffect(() => {
    fetch("http://localhost:1337/api/serial_data?rows=-1", {
      headers : {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
      }
    })
      .then(res => res.json())
      .then((res) => {
        console.log(res);
        if (res.length > 1){
          setData(res);
        } else{
          setData([res]);
        }
      })
      .catch(error => {
        setError(true);
        throw new Error(error);
      })
  },[]);

  return(
    <MyChart data={data} />
  );
};

export default Dashboard;