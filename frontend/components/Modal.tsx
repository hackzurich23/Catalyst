import React from "react";
import Modal from "react-modal";
import styles from "./Modal.module.css";

const customStyles = {
	content: { width: "60%", height: "fit-content", margin: "auto" },
};

interface IModal {
	isOpen: boolean;
	setIsOpen: (isOpen: boolean) => void;
	data: {
		questions?: string[];
		answers?: string[];
		contacts?: string[][];
		scores?: string;
	};
}

export const ModalComponent = ({ isOpen, setIsOpen, data }: IModal) => {
	let scores: number[] = [];

	try {
		scores = JSON.parse(data.scores || "[]");
		if (!Array.isArray(scores)) {
			scores = []; // Handle the case where the parsed result is not an array
		}
	} catch (error) {
		scores = []; // Handle JSON parsing errors
	}
	console.log(typeof data.scores);
	function openModal() {
		setIsOpen(true);
	}

	function afterOpenModal() {
		// references are now sync'd and can be accessed.
	}

	function closeModal() {
		setIsOpen(false);
	}

	return (
		<div>
			<Modal
				isOpen={isOpen}
				onAfterOpen={afterOpenModal}
				onRequestClose={closeModal}
				style={customStyles}
				contentLabel="Example Modal"
			>
				<h2
					style={{
						fontSize: 24,
						marginBottom: 14,
					}}
				>
					Sources:
				</h2>
				{data.questions?.map((question, index) => {
					console.log(scores[index]);
					return (
						<div key={index} className={styles.box}>
							<div className={styles.score}>{scores[index]}</div>
							<p className={styles.answer}>{data.answers?.[index]}</p>
							<p className={styles.question}>{question}</p>
							<div className={styles.ppl_box}>
								<div className={styles.people}>People present at the meeting:</div>
								{data.contacts?.[index].map((contact, index) => (
									<a
										key={index}
										href={contact}
										target="_blank"
										rel="noreferrer"
										className={styles.contact}
									>
										{"  "}
										{contact}
									</a>
								))}
							</div>
						</div>
					);
				})}
			</Modal>
		</div>
	);
};
