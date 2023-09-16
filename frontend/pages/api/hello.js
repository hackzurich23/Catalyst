import axios from "axios";

// eslint-disable-next-line import/no-anonymous-default-export
export default async (req, res) => {
	console.log(req.params);
	try {
		// todo: add the params
		const params = {
			message: "hello",
		};
		const response = await axios.get("http://localhost:3001/hello", { params });
		const data = response.data;

		res.json(data);
	} catch (error) {
		res.status(500).json({ error: "An error occurred while fetching data" });
	}
};
