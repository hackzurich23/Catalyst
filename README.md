![logo](https://res.cloudinary.com/dohxofaxb/image/upload/v1694894880/Wiki_1920_1280_px_nyecja.png)
# Table of Contents
- [CATALYST](#catalyst)
- [Inspiration](#inspiration)
- [What it does](#what-it-does)
- [How we built it](#how-we-built-it)
- [Challenges we ran into](#challenges-we-ran-into)
- [Accomplishments that we're proud of](#accomplishments-that-were-proud-of)
- [What we learned](#what-we-learned)
- [What's next for Catalyst](#whats-next-for-catalyst)
- [Installation](#installation)
- [ENV](#env)
- [Launch backend](#launch-backend)
- [Deployment](#deployment)
  - [Backend](#backend)
  - [Frontend](#frontend)


# CATALYST

We created _Catalyst_ to make the life of engineers, salespeople, HR staff, and others in a commercial environment easier. Catalyst continuously gathers the internal knowledge of an organization and makes it accessible to everyone. The way we built our solution provides opportunities to save time, know more, and reduce stress on the humans in the loop. Ultimately, this _catalyzes_ all business processes.

## Inspiration

We saw that employees of large businesses often spend a lot of time on the *hunt for information*, *stuck in meetings*, and *struggling with problems that someone within the company has solved before*. Moreover, we recognized that internal wikis and recordings of online meetings could be a valuable resource, but often remained underutilized due to the sheer volume and lack of organization. Thus, we wanted to create a tool to access this information quickly and easily, and learn from the experiences of others.

## What it does

Catalyst is a comprehensive platform comprising several key components:

1. **Data Collection**: Catalyst gathers and stores both internal and external company data from various sources. It also supplements this information with content from internal meetings.

2. **Data Pre-processing**: Following data cleansing, the system extracts pertinent details and organizes them into discrete facts. All these facts are stored in a **database**, enabling users to search for them using text queries.

3. **Chat Bot**: An AI model serves as an intermediary between the user and the data. It endeavors to comprehend user inquiries and formulates responses based on information from the database.

4. **User Interface, Trustworthiness, and Explainability**: The user interface constitutes the front-end website that facilitates user interactions with the system. We enhance transparency by offering detailed insights into how the chat bot generates responses, including the information from the database that was utilized and associated confidence scores.

## How we built it

Here's an overview of the key technologies and components used in Catalyst:

![System Design](https://res.cloudinary.com/dohxofaxb/image/upload/v1694894684/Wiki_qwizey.png)

- **Data Collection**: We implemented a Python bot using [Selenium](https://www.selenium.dev) that keeps track of scheduled meetings on [Google Calendar](https://calendar.google.com/calendar/u/0/r) and automatically joins those meetings on [Google Meet](https://meet.google.com). Meeting participants simply need to allow the bot to join. The bot **records the meeting, transcribes it and stores the result** in a [Google Drive](https://www.google.com/drive/). We complement this information with **Sika-specific external documents** that we obtained from [Sika USA](https://usa.sika.com)'s website.

- **Data Pre-processing**: We clean all textual data, summarize it and split it into facts using [OpenAI's API for ChatGPT](https://openai.com/blog/introducing-chatgpt-and-whisper-apis). We tried storing facts by themselves as well as in a question-and-answer format (hoping this would retain more context information), but did not see a qualitative difference.

- **Database & Chat Bot**: Inspired by works such as [DB-GPT](https://github.com/eosphoros-ai/DB-GPT), we also encode all data in a **vector database to make it searchable via chat** (FLAISS). We used the [LangChain](https://python.langchain.com/docs/get_started/introduction) framework to instantiate a context-aware ChatGPT model. This queries the database with the user's questions and uses the retrieved information to reason about the answer.

- **User Interface**: We created a web app using a [Flask](https://flask.palletsprojects.com/en/2.3.x/) backend and [React](https://react.dev) frontend. We built a chat interface for our conversational AI, an option to upload PDF files to the database, and the option to select different profiles that determine the security level of the data access. 

- **Trustworthiness & Explainability**: When querying from the vector database, we measure the distance between the query and the result and use this to compute our confidence score. Given an answer from the chat bot, we visualize the confidence score for every item retrieved from the database in the UI.

## Challenges we ran into

On the model side, using the vector database is challenging. Although there exist successful implementations of vector databases on large datasets, in our case, the retrieved text embeddings often do not correspond well to the user question that we query with. We tried embedding knowledge in different ways (as facts, Q&A, ...), but had little success in improving performance on this. Finally, the model is still able to answer questions about Sika, but only because ChatGPT was trained on data about it.

## Accomplishments that we're proud of

We are proud of the following achievements:

- Building a fully functional web app in less than 40 hours while having to tinker around with context-aware LLMs.
- Integrating data from multiple sources, which required building a bot for Google Meet.
- Development of an efficient chat assistant capable of providing instant solutions to common issues.
- Being part of HackZurich 2023.

## What we learned

During HackZurich the development of Catalyst, we learned the importance of:

- Planning the hackathon project starting from the demo. First, plan what the user requires, take into account what you want to/can show, and finally derive the set of features that have to be implemented from that.

- That working with LLMs and vector databases is pretty easy thanks to frameworks like LangChain, but the performance that we got out of the box was underwhelming.

- What to pack for the next hackathon :).

## What's next for Catalyst

In the future, we plan to:

- Expand data sources and integrations to enhance the richness of information available.
- Improve the encoding of the vector database. Others show that it can work better. It probably just requires reading more about it and trying some things.
- Extend the chat assistant's capabilities to handle a wider range of queries and tasks, such as multi-modal inputs (text, voice, etc.).

We believe that Catalyst has the potential to revolutionize the way people work and learn.

Challenge: Sika (New Approaches to Sika Knowledge Management)

## Installation

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
   cd project/timeline
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
