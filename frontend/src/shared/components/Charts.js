import React, { useState, useEffect } from "react";
import {
	LineChart,
	Line,
	XAxis,
	YAxis,
	CartesianGrid,
	Tooltip,
	Legend,
	ResponsiveContainer,
	BarChart,
	Bar,
	Brush,
} from "recharts";

import { parseEpoch } from "../utils/Parse";

const MyChart = (props) => {
	const [noData, setNoData] = useState(false);

	useEffect(() => {
		if (props.data == null) {
			setNoData(false);
			throw new Error("No data property supplied.");
		}
	}, []);

	// unix time formatting: https://github.com/recharts/recharts/issues/956
	// place this in respnsive container, doesn't work now
	return (
		<LineChart
			width={1000}
			height={300}
			data={props.data}
			margin={{
				top: 5,
				right: 30,
				left: 20,
				bottom: 5,
			}}
		>
			<CartesianGrid strokeDasharray="3 3" />
			<XAxis
				dataKey="time"
				tickFormatter={(timestamp) => parseEpoch(timestamp)}
			/>
			<YAxis padding={{ top: 30 }} />
			<Tooltip />
			<Legend stroke="#00000" />
			<Brush dataKey="time" height={40} stroke="#16a34a" />
			<Line
				type="monotone"
				dataKey="air_temp"
				dot={false}
				stroke="#16a34a"
			/>
		</LineChart>
	);
};

export default MyChart;
