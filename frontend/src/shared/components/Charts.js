import React, { useState,useEffect } from "react";
import {
  LineChart,
  Line,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend, 
  ResponsiveContainer,
} from "recharts";

import { extractDictItems, extractAirTemp } from "../utils/Array";

const MyChart = (props) => {
  const [noData, setNoData] = useState(false);

  useEffect(() => {
    if (props.data == null){
      setNoData(false);
      throw new Error("No data property supplied.");
    }
  },[]);

  //console.log(extractDictItems(props.data, 'air_temp'));
  {/* place this in respnsive container, doesn't work now */}
  return (
    <LineChart
      width={800}
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
        <YAxis key={Math.random()}/>
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="air_temp" />
    </LineChart>
  );
};

export default MyChart;