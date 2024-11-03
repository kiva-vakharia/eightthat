import { useState, useEffect } from "react";
import "./Beach.css";
import { Line } from "react-chartjs-2";
import Chart from "chart.js/auto";
import { CategoryScale } from "chart.js/auto";
import { useNavigate, useSearchParams } from "react-router-dom";

Chart.register(CategoryScale);
Chart.defaults.backgroundColor = "#000000";
Chart.defaults.color = "#000";

function Beach() {
	const [tides, setTide] = useState(null);
	const [weather, setWeather] = useState(null);
	let [searchParams, setSearchParams] = useSearchParams();
	const navigate = useNavigate();
	const beachName = searchParams.get("beach");

	async function getTideData(beach) {
		const res = await fetch(`/api/tide-data?beach_name=${beach}`);
		const data = await res.json();
		setTide(data);
	}

	async function getWeatherData(beach) {
		const res = await fetch(`/api/basic-weather-stats?beach_name=${beach}`);
		const data = await res.json();
		setWeather(data);
	}

	useEffect(() => {
		if (beachName) {
			getTideData(beachName);
			getWeatherData(beachName);
		} else {
			navigate("/");
		}
	}, []);

	return (
		<>
			<body class="beachyokay">
				<div style={{ width: "800px", height: "500px" }}>
					{tides && (
						<Line
							data={{
								labels: tides.map((t) =>
									new Date(t.timestamp.dt).toLocaleString("en-US")
								),
								datasets: [
									{
										label: "Tides",
										data: tides.map((t) => t.height),
										fill: {
											target: "origin",
											below: "rgb(100, 50, 3)",
										},
									},
								],
							}}
							options={{
								scales: {
									xAxes: [
										{
											type: "timeseries",
										},
									],
								},
							}}
						/>
					)}
				</div>
			</body>
			{weather && (
				<div>
					<wdata>Weather data for {beachName}</wdata>
					<atemp>Average temperature at beach: {weather.temp_now}</atemp>
					<weewee>
						Weather at {beachName}: {weather.desc}
					</weewee>{" "}
				</div>
			)}
		</>
	);
}

export default Beach;
