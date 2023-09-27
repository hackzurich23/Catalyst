import { useEffect, useRef, RefObject } from "react";
import { Avatar } from "./Avatar";

interface IDropdown {
	visible: boolean;
	setVisible: (visible: boolean) => void;
	role: string;
	setRole: (role: string) => void;
}

export const Dropdown = ({ visible, setVisible, role, setRole }: IDropdown) => {
	const roles = ["Intern", "Manager", "Dev"];
	const rolesToShow = roles.filter((r) => r !== role);
	const dropdownRef: RefObject<HTMLDivElement> = useRef(null); // Create a ref for the dropdown

	useEffect(() => {
		// Add a click event listener to the document
		const handleClickOutside = (event: any) => {
			if (dropdownRef.current) {
			  if (!dropdownRef.current.contains(event.target)) {
				setVisible(false); // Close the dropdown if the click is outside
			  }
			}
		};

		if (visible) {
			document.addEventListener("click", handleClickOutside);
		}

		// Remove the event listener when the component unmounts or the dropdown becomes invisible
		return () => {
			document.removeEventListener("click", handleClickOutside);
		};
	}, [visible, setVisible]);

	return (
		<div
			ref={dropdownRef} // Assign the ref to the dropdown
			style={{
				position: "absolute",
				top: 64,
				right: 0,
				width: "160px",
				borderRadius: "8px",
				overflow: "hidden",
				display: visible ? "block" : "none",
				backgroundColor: "transparent",
				zIndex: 1000,
			}}
		>
			{rolesToShow.map((r, index) => (
				<div
					key={index}
					style={{
						padding: "10px",
						backgroundColor: "white",
						cursor: "pointer",
					}}
					onClick={() => {
						setRole(r);
						setVisible(false); // Close the dropdown when an option is selected
					}}
				>
					{r}
				</div>
			))}
		</div>
	);
};

interface IEtiquette {
	dropDownVisible: boolean;
	setDropDownVisible: (dropDownVisible: boolean) => void;
	role: string;
}

export const Etiquette = ({ dropDownVisible, setDropDownVisible, role }: IEtiquette) => (
	<div
		style={{
			border: "4px solid hsl(204, 86%, 53%)",
			backgroundColor: "hsl(204, 86%, 53%)",
			width: "160px",
			display: "flex",
			justifyContent: "space-between",
			alignItems: "center",
			borderRadius: "100px",
			position: "relative",
			cursor: "pointer",
		}}
		onClick={() => {
			setDropDownVisible(!dropDownVisible);
		}}
	>
		<div
			style={{
				paddingLeft: "10px",
				flex: 1,
				color: "white",
				fontWeight: "bold",
				textAlign: "center",
			}}
		>
			{role}
		</div>
		<Avatar type={"user"} />
	</div>
);
