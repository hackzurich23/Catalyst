import axios from "axios";

// eslint-disable-next-line import/no-anonymous-default-export
export default async (req, res) => {
	const inputText = req.body.inputText;
	try {
		// todo: add the params
		const params = {
			message: inputText,
		};
		const response = await axios.get("http://localhost:8080/task", { params });
		const data = response.data;

		res.json(data);
	} catch (error) {
		res.status(500).json({ error: "An error occurred while fetching data" });
	}
};
