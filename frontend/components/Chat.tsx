"use client";
import React from "react";

import { Input } from "./Input";
import { IMessageElement, MessageElement } from "./MessageElement";

export const Chat = () => {
	const [messages, setMessages] = React.useState<IMessageElement[]>([
		// {
		// 	type: "bot",
		// 	text: "Hello, what can I do for you?",
		// },
	]);
	console.log(messages);
	const [data, setData] = React.useState("");
	const [inputText, setInputText] = React.useState("");

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
				await postFackMessage();
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
		try {
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
			} as IMessageElement;

			setMessages((prevMessages) => [...prevMessages, newMessage]);
			scrollToBottom();
		} catch (error) {
			console.error("An error occurred while sending the message", error);
			throw error; // Rethrow the error to handle it in the caller (handleSendMessage)
		}
	};

	const postFackMessage = async () => {
		try {
			const params = {
				inputText: inputText,
			};

			const response = await fetch("/api/hello", {
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
			} as IMessageElement;

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
			const container = messagesContainerRef.current;
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
					height: "70%",
					alignSelf: "center",
				}}
			>
				<div
					ref={messagesContainerRef} // Assign the ref to the messages container
					style={{ flex: 1, overflowY: "scroll" }}
				>
					{messages.length ? (
						messages.map((message, index) => (
							<MessageElement key={index} type={message.type} text={message.text} />
						))
					) : (
						<div
							style={{
								backgroundColor: "#dbd9d9",
								height: "100%",
								width: "100%",
								borderRadius: 8,
								padding: "12%",
								// greyish background
								// center elements horizontally and vertically
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
									// border: "1px solid black",
									// flex: 1,
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
						<button
							className="button is-primary"
							onClick={() => {
								handleSendMessage();
							}}
							title="Send"
							// change height of the button
							style={{
								height: "100%",
								marginLeft: "10px",
							}}
						>
							Send
						</button>
					</div>
				</div>
			</div>
			<p>{data}</p>
		</section>
	);
};
