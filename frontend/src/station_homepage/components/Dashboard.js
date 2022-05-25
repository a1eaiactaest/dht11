import React, { useEffect, useState } from "react";

//import { extractDictItems } from "../../shared/utils/Array";
import MyChart from "../../shared/components/Charts";
import NewChart from "../../shared/components/NewCharts";

const Dashboard = (props) => {
	const [data, setData] = useState([]);
	const [error, setError] = useState(false);

	// This urls fetch ALL POSSIBLe data for certain stations.

	useEffect(() => {
		let fetchURL = "";
		let station = props.station;

		if (station == 0) {
			fetchURL = "http://localhost:1337/api/serial_data?rows=-1";
		} else {
			fetchURL = `http://localhost:1337/api/serial_data?rows=-1&station=${props.station}`;
		}

		console.log(fetchURL);
		fetch(fetchURL, {
			headers: {
				"Content-Type": "application/json",
				Accept: "application/json",
			},
		})
			.then((res) => res.json())
			.then((res) => {
				console.log(res);
				if (res.length > 1) {
					setData(res);
				} else {
					setData([res]);
				}
			})
			.catch((error) => {
				setError(true);
				throw new Error(error);
			});
	}, []);

	return (
		<>
			<MyChart data={data} />
			<NewChart data={data} />
		</>
	);
};

export default Dashboard;
