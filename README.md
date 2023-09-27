![logo](https://res.cloudinary.com/dohxofaxb/image/upload/v1694894880/Wiki_1920_1280_px_nyecja.png)

Created during HackZurich 2023 (Sika Challenge). | [[Devpost](https://devpost.com/software/timemachine-qux19t)] | [[Winner Photo](https://www.linkedin.com/feed/update/urn:li:activity:7110164700285296641/)]

# What it does

Catalyst gathers and stores company data from PDFs, wikis and meeting transcriptions. It cleans the data and organizes knowledge into discrete facts. All these facts are stored in a **vector database**, enabling users to search for them using text queries. A ChatGPT-powered chat-bot comprehends user inquiries and formulates responses based on information from the database. We enhance transparency by offering detailed insights into how the chat bot generates responses, including the information from the database that was utilized and associated confidence scores.

# Installation

To set up the project, follow these steps:

1. Install

 the required Python packages by running the following command in the project's root directory:

   ```bash
   pip install -r backend/requirements.txt
   ```

2. Configure Environment Variables:
   - The project utilizes the `gpt-3.5-turbo-16k-0613` model. To gain access to it, you must specify your `OPENAI_API_KEY` in the `.env` file.
   - Additionally, you need to provide the bot's Google credentials in the `.env` file.

## Launch backend

To start the backend server, navigate to the project's root directory (in the 'timeline' folder) and execute the following command:

```bash
python backend/app.py
```

## Deployment

### Backend

For proper deployment, follow these steps:

1. Activate the virtual environment (venv) with the following command:

   ```bash
   cd project/Catalyst
   source myvenv/bin/activate
   ```

2. To serve the Flask backend in debug mode, run:

   ```bash
   python backend/app.py
   ```

### Frontend

For proper deployment, run the following command from the ./frontend directory.

   ```bash
   npm run dev
   ```

The API can be accessed using the external ID of the VM followed by port `3000`.

### Docker

Building the Docker container (combines frontend and backend):
```bash
docker build -f Dockerfile.combined -t catalyst-combined .
```

Running the Docker images:
```bash
docker run --rm -p 3000:3000 catalyst-combined
```
