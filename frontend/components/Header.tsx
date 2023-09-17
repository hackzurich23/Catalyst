"use client";
import Link from "next/link";
import { Avatar } from "./Avatar";
import { usePathname } from "next/navigation";
import Image from "next/image";
import { Dropdown, Etiquette } from "./Dropdown";
import React from "react";

export const Header = () => {
	// get current page
	const path = usePathname();
	const [dropDownVisible, setDropDownVisible] = React.useState(false);
	const [role, setRole] = React.useState("Intern");

	return (
		<section className="section">
			<div
				className="container"
				style={{
					display: "flex",
					alignItems: "center",
					justifyContent: "space-between",
				}}
			>
				<Link href="/">
					<Image src="/logo.svg" alt={""} width={320} height={110} />
				</Link>
				<div
					style={{
						display: "flex",
						alignItems: "center",
						justifyContent: "space-between",
					}}
				>
					{path != "/" ? (
						<Link href="/">
							<button className="button is-link mr-6 is-light">
								<p>Chat</p>
							</button>
						</Link>
					) : (
						<Link href="/upload" style={{ color: "white" }}>
							<button className="button is-link mr-6 is-light">
								<p>Add more knowledge</p>
							</button>
						</Link>
					)}
					<Etiquette
						dropDownVisible={dropDownVisible}
						setDropDownVisible={setDropDownVisible}
						role={role}
					/>
					<Dropdown
						visible={dropDownVisible}
						setVisible={setDropDownVisible}
						setRole={setRole}
						role={role}
					/>
				</div>
			</div>
		</section>
	);
};
