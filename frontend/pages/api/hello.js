import axios from "axios";

// eslint-disable-next-line import/no-anonymous-default-export
export default async (req, res) => {
	console.log("hello");
	try {
		// todo: add the params
		const params = {
			message: "hello",
		};
		console.log(process.env.API_URL);
		const response = await axios.get(process.env.API_URL + "/hello", { params });
		const data = response.data;

		res.json(data);
	} catch (error) {
		res.status(500).json({ error: "An error occurred while fetching data" });
	}
};
