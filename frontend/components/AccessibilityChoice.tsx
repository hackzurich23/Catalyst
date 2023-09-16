import React, { useState } from "react";
import "@/styles/AccessibilityChoice.css";

export const AccessibilityChoice = () => {
	// Define state variables to track the button states
	const [anyone, setAnyone] = useState(false);
	const [internalUsers, setInternalUsers] = useState(false);
	const [developers, setDevelopers] = useState(false);
	const [salesPeople, setSalesPeople] = useState(false);

	return (
		<section className="section">
			<h2 className="subtitle">Accessibility:</h2>

			{/* Button for Anyone */}
			<button
				className={`accessibility-button ${anyone ? "active" : ""}`}
				onClick={() => {
					setAnyone(!anyone);
					// Deactivate other buttons when "Anyone" is activated
					setInternalUsers(false);
					setDevelopers(false);
					setSalesPeople(false);
				}}
			>
				Anyone
			</button>

			{/* Button for Internal Users */}
			<button
				className={`accessibility-button ${internalUsers ? "active" : ""}`}
				onClick={() => {
					setInternalUsers(!internalUsers);
					// Deactivate "Anyone" button when "Internal Users" is activated
					setAnyone(false);
				}}
			>
				Internal Users
			</button>

			{/* Button for Developers */}
			<button
				className={`accessibility-button ${developers ? "active" : ""}`}
				onClick={() => {
					setDevelopers(!developers);
				}}
			>
				Developers
			</button>

			{/* Button for Salespeople */}
			<button
				className={`accessibility-button ${salesPeople ? "active" : ""}`}
				onClick={() => {
					setSalesPeople(!salesPeople);
				}}
			>
				Salespeople
			</button>
		</section>
	);
};
