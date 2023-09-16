import streamlit as st
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
from langchain.vectorstores import Chroma
import chromadb
import uuid
from chromadb.utils import embedding_functions
from flask import Flask, request, jsonify
import os
from meeting_participant import launch_bot
from prompts import BOT_SYSTEM_PROMPT

from text2summary import Text2Summary
from faiss_db import FAISS_DB
from data.transcripts import ALL_MEETINGS
from llm import LLM

# from meeting_participant import AskToJoin

# TODO: clean the code!!!!!
# Define global variables:
app = Flask(__name__)

# Initial setup: DB & model initialization...
load_dotenv()

# 1. Vectorize the sales response csv data
# TODO: our extracted Q&A DB:
# loader = CSVLoader(file_path="test-langchain/generated_q_and_a_correct.csv")
# documents = loader.load()
# embeddings = OpenAIEmbeddings()
# TODO: save BD to disk or load it from disk depending on if file exists
# the Chroma DB causes some troubles again so for the simplicity let's use FAISS
# db = Chroma.from_documents(documents, embeddings, persist_directory="chroma_db_old_version")
# db = FAISS.from_documents(documents, embeddings)
faiss_db = FAISS_DB()

# 3. Setup LLMChain & prompts
# llm = ChatOpenAI(temperature=0, model=os.getenv('MODEL_OLD'))
# prompt = PromptTemplate(
#     input_variables=["message", "best_practice"],
#     template=BOT_SYSTEM_PROMPT
# )
# chain = LLMChain(llm=llm, prompt=prompt)
educated_llm = LLM()

# load DB from disk
# db = Chroma(persist_directory="chroma_db", embedding_function=embeddings)


# 5. Build an app with streamlit
def main():
    app.run(debug=True, host="0.0.0.0", port=3001)
    # st.set_page_config(
    #     page_title="Customer response generator", page_icon=":bird:")
    #
    # st.header("Customer response generator :bird:")
    # message = st.text_area("customer message")
    #
    # if message:
    #     st.write("Generating best practice message...")
    #
    #     result = generate_response(message)
    #
    #     st.info(result)


#     FLASK ROUTES
@app.route('/task', methods=['GET'])
def calculate_task():
    # Get the query parameters
    role = request.args.get('role', type=str)
    task_type = request.args.get('task_type', type=str)
    message = request.args.get('message', type=str)
    # TODO: define DB depending on the user's role and define prompt depending on the task_type
    response, education, metadata, scores = educated_llm.get_educated_response(faiss_db, message)
    json_ret = jsonify({
        'output': response,
        "education": education,
        "scores": scores,
        "links": [_["link"] for _ in metadata],
        "contacts": [_["contacts"] for _ in metadata],
    })
    return json_ret


@app.route('/hello', methods=['GET'])
def basic():
    return jsonify({'output': "Martin jopa"})

@app.route('/join-meeting', methods=['GET'])
def join_meeting():
    meeting_id = request.args.get('meeting-id', type=str)
    print(os.getenv('SELENIUM_GMAIL'))
    print(os.getenv('SELENEUM_GPASSWORD'))
    launch_bot(os.getenv('SELENIUM_GMAIL'), os.getenv('SELENEUM_GPASSWORD'), meeting_id)

    return jsonify({'output': "did we log in???"})


if __name__ == '__main__':
    main()
