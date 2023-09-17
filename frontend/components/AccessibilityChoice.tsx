import React, { useState } from "react";

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
				className={`
					button is-link mr-4
				${anyone ? "is-link-light" : ""}`}
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
				className={`button is-link mr-4 ${internalUsers ? "is-light" : ""}`}
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
				className={`button is-link mr-4 ${developers ? "is-light" : ""}`}
				onClick={() => {
					setDevelopers(!developers);
				}}
			>
				Developers
			</button>

			{/* Button for Salespeople */}
			<button
				className={`button is-link mr-4 ${salesPeople ? "is-light" : ""}`}
				onClick={() => {
					setSalesPeople(!salesPeople);
				}}
			>
				Salespeople
			</button>
		</section>
	);
};
