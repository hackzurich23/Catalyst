import React from "react";
import Modal from "react-modal";
import styles from "./Modal.module.css";

const customStyles = {
	content: {
		width: "60%",
		height: "fit-content",
		margin: "auto",
		border: "2px solid grey",
		borderRadius: 8,
	},
};

interface IModal {
	isOpen: boolean;
	setIsOpen: (isOpen: boolean) => void;
	data: {
		questions?: string[];
		answers?: string[];
		contacts?: string[][];
		scores?: string[];
		links?: string[];
		type?: string;
	};
}

export const ModalComponent = ({ isOpen, setIsOpen, data }: IModal) => {
	const scores = data.scores;
	console.log(data);

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
					return (
						<div key={index} className={styles.box}>
							<div className={styles.score}>{(Number(scores?.[index] || 0) * 100).toFixed(2)}%</div>
							<p className={styles.answer}>{data.answers?.[index]}</p>
							<p className={styles.question}>{question}</p>
							{data.type === "meeting" ? (
								<div className={styles.ppl_box}>
									<div className={styles.people}>
										People present at the meeting:
									</div>
									{data.contacts?.[index]?.map((contact, index) => (
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
							) : (
								<div className={styles.ppl_box}>
									<div className={styles.people}>Files that might be useful:</div>
									{/* Get list of links */}
									{data.links?.map((contact, index) => (
										<a
											key={index}
											href={contact}
											target="_blank"
											rel="noreferrer"
											className={styles.contact}
										>
											{"  "}
											{"link " + (index + 1)}
										</a>
									))}
									{/* <ul>
										{data.links?.map((contact, index) => {
											console.log(contact);
											return (
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
											);
										})}
									</ul> */}
								</div>
							)}
							{/* <div className={styles.ppl_box}>
								<div>You can find more with those links:</div>
								{data.links}
							</div> */}
						</div>
					);
				})}
			</Modal>
		</div>
	);
};
