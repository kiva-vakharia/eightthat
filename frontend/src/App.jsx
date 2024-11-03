import { useNavigate } from "react-router-dom";
import "./App.css";
import testing from "./assets/petrsurf2.gif";
import sunny from "./assets/sunset.svg";
import logo2 from "./assets/logocartoon.png";
import { Navigate } from "react-router-dom";

const beachNames = [
	"The Wedge",
	"Corona Del Mar",
	"Newport Point",
	"Blackies",
	"Newport Lower Jetties",
	"Crystal Cove",
	"Newport Upper Jetties",
	"River Jetties",
	"Crescent Bay",
	"Rockpile",
	"Huntington State Beach",
	"Thalia Street",
	"Brooks Street",
	"Huntington St.",
	"Agate Street",
	"Huntington Beach Pier Southside",
	"North HB",
	"Aliso Creek",
	"HB Cliffs",
];

function App() {
	const navigate = useNavigate();

	return (
		<>
			<img src={testing} className="mainthing" />
			<bounce>
				<img src={logo2} className="logo"></img>
			</bounce>
			<p>Select a beach</p>
			<select
				name="beachNames"
				id="beach"
				class="dropbtn"
				onChange={(e) => navigate(`/beach?beach=${e.target.value}`)}
			>
				{beachNames.map((beach) => (
					<option key={beach}> {beach}</option>
				))}
				<option key="." selected>
					...
				</option>
			</select>
		</>
	);
}

export default App;
