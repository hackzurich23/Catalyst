import React from "react";
import { ModalComponent } from "./Modal";
import { Avatar } from "./Avatar";
import { Button } from "./Button";

// messageOrigin can be 'user' or 'bot'
export interface IMessageElement {
	type: "user" | "bot";
	text: string;
	questions?: string[];
	answers?: string[];
	contacts?: string[][];
	scores?: string[];
	links?: string[];
}

export const MessageElement = (props: IMessageElement) => {
	const { type, text, questions, answers, contacts, scores, links } = props;
	const [modalIsOpen, setIsOpen] = React.useState(false);
	return (
		<section
			className="section"
			style={{
				display: "flex",
				width: "100%",
				padding: 0,
				backgroundColor: type === "user" ? "white" : "#ebe8e8",
				flexDirection: type === "user" ? "row-reverse" : "row",
				alignContent: "center",
			}}
		>
			<div style={{ padding: 5 }}>
				{type == "user" ? <Avatar type={"user"} /> : <Avatar type={"bot"} />}
			</div>

			<div>
				<div
					style={{
						width: "fit-content",
						padding: 12,
					}}
				>
					{text}
				</div>
				{type == "bot" && questions && (
					<button
						className="button is-small"
						style={{ marginLeft: 8, marginBottom: 4 }}
						onClick={() => setIsOpen(true)}
					>
						See more
					</button>
				)}
				<ModalComponent
					isOpen={modalIsOpen}
					setIsOpen={setIsOpen}
					data={{ questions, answers, contacts, scores, links, type }}
				/>
			</div>
		</section>
	);
};
