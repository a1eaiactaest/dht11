import React, { Component } from "react";
import ReactApexChart from "react-apexcharts";

import { extractDictItems } from "../utils/Array";

const NewChart = (props) => {
  const yAxisData = extractDictItems(props.data, "air_temp");
  const xAxisData = extractDictItems(props.data, "time");

  const series = [
    {
      name: "Temperature in Celcius",
      data: yAxisData,
    },
  ];

  const options = {
    chart: {
      height: 350,
      type: "line",
      zoom: {
        enabled: true,
      },
      stroke: {
        curve: "smooth",
      },
      xaxis: {
        type: "datetime",
        categories: [1, 2, 3, 4, 3, 1, 5],
        labels: {
          formatter: function (value, timestamp) {
            return new Date(timestamp * 1000);
          },
        },
      },
    },
  };

  return (
    <ReactApexChart
      options={options}
      series={series}
      height={350}
      width="80%"
    />
  );
};

export default NewChart;
