// components/ApiData.js
"use client";
import React, { useEffect, useState } from "react";

const FetchApiComponent = () => {
	const [data, setData] = useState(null);

	useEffect(() => {
		// Define the API endpoint URL
		const apiUrl = "/api/proxy"; // Replace with your API URL

		fetch(apiUrl)
			.then((res) => res.json())
			.then((data) => {
				setData(data.output);
			})
			.catch((err) => {
				console.error("An error occurred", err);
			});
	}, []);

	return (
		<section className="section">
			<h2>API Data:</h2>
			<p>{data}</p>
		</section>
	);
};

export default FetchApiComponent;
function axios(
	apiUrl: string,
	arg1: {
		headers: { "Content-Type": string; Accept: string; "Access-Control-Allow-Origin": string };
		method: string;
	}
) {
	throw new Error("Function not implemented.");
}
