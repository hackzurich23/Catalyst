import { Chat } from "@/components/Chat";
import { Layout } from "@/components/Layout";
import "react-chat-elements/dist/main.css";

export default function Home() {
	return (
		<Layout>
			<Chat />
		</Layout>
	);
}
