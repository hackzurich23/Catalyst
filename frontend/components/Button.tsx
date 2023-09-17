import styles from "./Button.module.css";

interface IButton {
	onClick: () => void;
	text: string;
	style?: any;
}

export const Button = ({ onClick, text, style }: IButton) => {
	return (
		<button className={[styles.button, style].join(" ")} onClick={onClick}>
			<p>{text}</p>
		</button>
	);
};
