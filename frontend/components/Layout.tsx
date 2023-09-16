import { Header } from "./Header";
import "bulma/css/bulma.css";

export const Layout = ({ children }: { children?: any }) => (
	<section
		style={{
			height: "100%",
			display: "flex",
			flexDirection: "column",
			overflow: "hidden",
			backgroundColor: "#f5f5f5",
			minHeight: "100vh",
		}}
	>
		<Header />
		{children}
	</section>
);
