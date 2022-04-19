import React, { useState,useEffect } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend, 
} from "recharts";


const MyChart= (props) => {
  const [noData, setNoData] = useState(false);

  useEffect(() => {
    if (props.data == null){
      setNoData(false);
      throw new Error("No data property supplied.");
    }
  },[]);

  {/* Chart Parameters */}

  return (
    <LineChart
      width={500}
      height={500}
      data={props.data}
      margin={{
        top: 5,
        right: 30,
        left: 20,
        bottom: 5,
      }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey=""/>
        <YAxis />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="air_temp" />
    </LineChart>
  );
};

export default MyChart;