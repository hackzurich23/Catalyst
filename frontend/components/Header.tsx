import Link from "next/link";
import { Avatar } from "./Avatar";

export const Header = () => {
	return (
		<section className="section">
			<div
				className="container"
				style={{ display: "flex", alignItems: "center", justifyContent: "space-between" }}
			>
				<Link href="/">
					<p className="title">Our Super App</p>
				</Link>

				<button style={{ border: "none", backgroundColor: "transparent" }}>
					<Avatar type={"user"} />
				</button>
			</div>
		</section>
	);
};
