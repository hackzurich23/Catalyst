import Image from "next/image";

export const Avatar = ({ type }: { type: "bot" | "user" }) => {
	return (
		<div style={{ width: "40px", height: "40px", borderRadius: "100px", overflow: "hidden" }}>
			{type == "user" ? (
				<Image src="/profile.jpg" alt="W3Schools.com" width={40} height={40} />
			) : (
				<Image src="/bot.jpg" alt="W3Schools.com" width={40} height={40} />
			)}
		</div>
	);
};
