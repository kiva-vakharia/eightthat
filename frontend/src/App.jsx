import { useNavigate } from "react-router-dom";
import "./App.css";

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
			{beachNames.map((beach) => (
				<button key={beach} onClick={() => {
					navigate(`/beach?beach=${beach}`)
				}}>{beach}</button>
			))}
		</>
	);
}

export default App;
