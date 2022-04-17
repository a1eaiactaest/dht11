import React, { useState,useEffect } from "react";

import { 
  Chart, 
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from "chart.js";
import { Line } from "react-chartjs-2";

Chart.register(
  CategoryScale,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

export const DefaultChartOptions = {
  responsive: true,
  plugins: {
    title: {
      display: true,
      text: 'RERE Chart',
    },
  },
}

const LineChart = (props) => {
  const [noption, setNoption] = useState(false);

  useEffect(() => {
    if (props.options == null){
      setNoption(true);
    }
  },[]);

  return (
    <Line 
      options={noption ? DefaultChartOptions : props.options}
      data={{
        labels: ["asfd","asdf"],
        datasets: [props.data]
      }}
    />
  );
};

export default LineChart;