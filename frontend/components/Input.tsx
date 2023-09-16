import styles from "./Input.module.css";

interface IInput {
	handleInputKeyPress: (e: any) => void;
	handleInputTextChange: (e: any) => void;
	inputText: string;
}

export const Input = ({ handleInputKeyPress, handleInputTextChange, inputText }: IInput) => {
	return (
		<div className="input-container" style={{ flex: 1 }}>
			<input
				className={styles.input}
				type="text"
				placeholder="Type a message..."
				value={inputText}
				onChange={handleInputTextChange}
				onKeyPress={handleInputKeyPress}
			/>
		</div>
	);
};
