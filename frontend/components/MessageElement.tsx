// messageOrigin can be 'user' or 'bot'

export interface IMessageElement {
	type: "user" | "bot";
	text: string;
}

export const MessageElement = ({ type, text }: IMessageElement) => {
	return (
		<section
			className="section"
			style={{
				display: "flex",
				flexDirection: "column",
				width: "100%",
				padding: 0,
				alignItems: type === "user" ? "flex-end" : "flex-start",
				// use light grayish colors
				backgroundColor: type === "user" ? "#f5f5f5" : "#e0e0e0",
				borderRadius: 4,
			}}
		>
			<div
				style={{
					width: "fit-content",
					padding: 12,
					// color: "white",
					// fontWeight: "bold",
				}}
			>
				{text}
			</div>
		</section>
	);
};
