"use client";
import React from "react";

import { Input } from "./Input";
import { IMessageElement, MessageElement } from "./MessageElement";
import { Button } from "./Button";
import Image from "next/image";

export const Chat = () => {
	const [messages, setMessages] = React.useState<IMessageElement[]>([]);

	const [data, setData] = React.useState("");
	const [inputText, setInputText] = React.useState("");

	const [loading, setLoading] = React.useState(false);

	const handleInputTextChange = (e: any) => {
		setInputText(e.target.value);
	};

	const handleSendMessage = async () => {
		if (inputText.trim() !== "") {
			// Create a new message object
			const newMessage = {
				type: "user",
				text: inputText,
			} as IMessageElement;

			try {
				setMessages((prevMessages) => [...prevMessages, newMessage]);
				setInputText("");
				await postMessage();
				scrollToBottom();
			} catch (error) {
				console.error("An error occurred while sending the message", error);
				// Handle the error, e.g., display an error message to the user
			}
		}
		scrollToBottom();
	};

	// Handle sending messages on Enter key press
	const handleInputKeyPress = (e: any) => {
		if (e.key === "Enter") {
			handleSendMessage();
		}
	};

	const fetchApi = () => {
		const apiUrl = "/api/hello"; // Replace with your API URL
		fetch(apiUrl)
			.then((res) => res.json())
			.then((data) => {
				setData(data.output);
			})
			.catch((err) => {
				console.error("An error occurred", err);
			});
	};

	const postMessage = async () => {
		console.log("postMessage");
		try {
			setLoading(true);

			const params = {
				inputText: inputText,
			};

			const response = await fetch("/api/task", {
				method: "POST",
				headers: {
					"Content-Type": "application/json",
				},
				body: JSON.stringify(params),
			});

			if (!response.ok) {
				throw new Error(`HTTP error! Status: ${response.status}`);
			}

			const botAnswer = await response.json();
			console.log("botAnswer:", botAnswer);
			// print new message from the bot
			const newMessage = {
				type: "bot",
				text: botAnswer.output,
				questions: botAnswer.questions,
				answers: botAnswer.answers,
				contacts: botAnswer.contacts,
				scores: botAnswer.scores,
				links: botAnswer.links,
			} as IMessageElement;

			setLoading(false);
			setMessages((prevMessages) => [...prevMessages, newMessage]);
			scrollToBottom();
		} catch (error) {
			console.error("An error occurred while sending the message", error);
			throw error; // Rethrow the error to handle it in the caller (handleSendMessage)
		}
	};

	const postFakeMessage = async () => {
		try {
			setLoading(true);
			const botAnswer = {
				answers: [
					"Testing how Google reacts to speaking with different voices.",
					"He says 'my God'.",
					"The meeting.",
					"A model for assigning voices to accounts.",
					"To save the meeting.",
				],
				contacts: [
					["John Cena", "Jane", "Spoderman"],
					["John Cena", "Jane", "Spoderman"],
					["John Cena", "Jane", "Spoderman"],
					["John Cena", "Jane", "Spoderman"],
					["John Cena", "Jane", "Spoderman"],
				],
				links: [
					"https://docs.google.com/document/d/1zCIHmP6lrKfTaMvZmKiZEivl3CBGtcBdBg3Ob3-sa4c/edit?usp=sharing",
					"https://docs.google.com/document/d/1zCIHmP6lrKfTaMvZmKiZEivl3CBGtcBdBg3Ob3-sa4c/edit?usp=sharing",
					"https://docs.google.com/document/d/1zCIHmP6lrKfTaMvZmKiZEivl3CBGtcBdBg3Ob3-sa4c/edit?usp=sharing",
					"https://docs.google.com/document/d/1zCIHmP6lrKfTaMvZmKiZEivl3CBGtcBdBg3Ob3-sa4c/edit?usp=sharing",
					"https://docs.google.com/document/d/1zCIHmP6lrKfTaMvZmKiZEivl3CBGtcBdBg3Ob3-sa4c/edit?usp=sharing",
				],
				output: "Hello,\n\nThank you for reaching out to us. We appreciate your interest in our company. How can I assist you today?\n\nBest regards,\n[Your Name]",
				questions: [
					"What is the main topic of the meeting?",
					"What is Martin Tefra's reaction?",
					"What are they considering closing?",
					"What third-party model are they using?",
					"What is the purpose of pressing the button after two minutes?",
				],
				scores: '"[0.46665528, 0.47757202, 0.51060057, 0.5208136, 0.5381808]"',
			};
			// print new message from the bot
			const newMessage = {
				type: "bot",
				text: botAnswer.output,
				questions: botAnswer.questions,
				answers: botAnswer.answers,
				contacts: botAnswer.contacts,
				scores: JSON.parse(botAnswer.scores), // Parse the scores string into an array
			} as IMessageElement;

			setLoading(false);
			setMessages((prevMessages) => [...prevMessages, newMessage]);
			scrollToBottom();
		} catch (error) {
			console.error("An error occurred while sending the message", error);
			throw error; // Rethrow the error to handle it in the caller (handleSendMessage)
		}
	};

	React.useEffect(() => {
		// fetch messages from the server
		// fetchApi();
		scrollToBottom();
	}, [messages]);

	const messagesContainerRef = React.useRef(null);

	const scrollToBottom = () => {
		if (messagesContainerRef.current) {
		  const container: HTMLDivElement = messagesContainerRef.current; // Define the type for the container
		  container.scrollTop = container.scrollHeight;
		}
	};

	return (
		<section
			className="section box-shadow"
			style={{ display: "flex", flexDirection: "column", height: "100%" }}
		>
			<div
				style={{
					flex: 1,
					display: "flex",
					flexDirection: "column",
					position: "absolute",
					bottom: "0",
					marginBottom: 40,
					width: "70%",
					height: "75%",
					alignSelf: "center",
				}}
			>
				<div
					ref={messagesContainerRef} // Assign the ref to the messages container
					style={{ flex: 1, overflowY: "scroll" }}
				>
					{messages.length ? (
						<>
							{messages.map((message, index) => (
								<MessageElement
									key={index}
									type={message.type}
									text={message.text}
									questions={message.questions}
									answers={message.answers}
									contacts={message.contacts}
									scores={message.scores}
									links={message.links}
								/>
							))}
							{loading && (
								<Image
									src="/three-dots.svg"
									height={30}
									width={30}
									alt={"loading points"}
									style={{
										margin: "10px",
										filter: "invert(40%) sepia(95%) saturate(2374%) hue-rotate(166deg) brightness(101%) contrast(103%)",
									}}
								/>
							)}
						</>
					) : (
						<div
							style={{
								backgroundColor: "#ebe8e8",
								height: "100%",
								width: "100%",
								borderRadius: 8,
								padding: "12%",
								border: "3px solid rgb(32, 156, 238, 0.5)",
								// #209cee",
								display: "flex",
								justifyContent: "space-around",
								alignItems: "center",
								flexDirection: "column",
							}}
						>
							<p style={{ fontSize: "30px" }}>
								Write any question to start the conversation:
							</p>
							{/* examples of what to ask  */}
							<div
								style={{
									display: "flex",
									justifyContent: "space-around",
									flexDirection: "column",
									fontSize: "20px",
									height: "30%",
								}}
							>
								<p>
									What products can I use to repear a crack in my swimming pool ?
								</p>
								<p>Where can I find the documentation about the new project ?</p>
							</div>
						</div>
					)}
				</div>
				<div style={{ justifyContent: "flex", flexDirection: "row", marginTop: "20px" }}>
					<div
						style={{
							display: "flex",
							alignItems: "center",
						}}
					>
						<Input
							inputText={inputText}
							handleInputTextChange={handleInputTextChange}
							handleInputKeyPress={handleInputKeyPress}
						/>
						<Button
							onClick={() => {
								handleInputKeyPress({ key: "Enter" });
							}}
							text={"Send"}
						></Button>
					</div>
				</div>
			</div>
			<p>{data}</p>
		</section>
	);
};
