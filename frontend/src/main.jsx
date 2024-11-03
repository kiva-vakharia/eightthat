import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./index.css";
import Beach from "./Beach.jsx";

/*
This code renders our project so it can be viewed in a browser. 
*/

const router = createBrowserRouter([
	{
		path: "/",
		element: <App />,
	},
	{
		path: "/beach",
		element: <Beach />,
	},
]);

ReactDOM.createRoot(document.getElementById("root")).render(
	<React.StrictMode>
		<RouterProvider router={router} />
	</React.StrictMode>
);
