import Link from "next/link";

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
				<div>
					<Link href="/upload" style={{ color: "white" }}>
						<button className="button is-primary mr-2">
							<p>Add files</p>
						</button>
					</Link>
					<button className="button is-link">Account</button>
				</div>
			</div>
		</section>
	);
};
