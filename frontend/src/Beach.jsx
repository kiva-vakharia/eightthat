import { useState, useEffect } from "react";
import "./Beach.css";
import { Line } from "react-chartjs-2";
import Chart from "chart.js/auto";
import { CategoryScale } from "chart.js/auto";
import { useNavigate, useSearchParams } from "react-router-dom";

Chart.register(CategoryScale);

function Beach() {
	const [tides, setTide] = useState(null);
	let [searchParams, setSearchParams] = useSearchParams();
	const navigate = useNavigate();

	async function getTideData(beach) {
		const res = await fetch(`/api/tide-data?beach_name=${beach}`);
		const data = await res.json();
		setTide(data);
	}

	useEffect(() => {
		// getTideData();
		const valid = searchParams.get("beach");
		if (valid) {
			getTideData(valid);
		} else {
			navigate("/");
		}
	}, []);

	return (
		<>
		BEACH!!!!!!!
			{tides && (
				<div style={{width: "800px", height: "500px"}}>
				<Line
					data={{
						labels: tides.map((t) => new Date(t.timestamp.dt).toLocaleString('en-US', )),
						datasets: [
							{
								label: "Tides",
								data: tides.map((t) => t.height),
								fill: {
									target: "origin",
									below: "rgb(0, 0, 255)",
								},
							},
						],
					}}
					options={{
						plugins: { title: { display: true, text: "Hi" } },
						scales: {
							xAxes: [
								{
									type: "timeseries",
								},
							],
						},
					}}
				/>
				</div>
			)}
		</>
	);
}

export default Beach;
