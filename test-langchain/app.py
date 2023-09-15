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
from meeting_participant import AskToJoin

# TODO: clean the code!!!!!
# Define global variables:
app = Flask(__name__)

# Initial setup: DB & model initialization...
load_dotenv()

# 1. Vectorise the sales response csv data
# TODO: our extracted Q&A DB:
loader = CSVLoader(file_path="generated_q_and_a_correct.csv")
documents = loader.load()
embeddings = OpenAIEmbeddings()
# TODO: save BD to disk or load it from disk depending on if file exists
db = Chroma.from_documents(documents, embeddings, persist_directory="chroma_db_old_version")

# 3. Setup LLMChain & prompts
llm = ChatOpenAI(temperature=0, model=os.getenv('MODEL_OLD'))

template = """
        You are a world class business development representative.
        I will share a prospect's message with you and you will give me the best answer that
        I should send to this prospect based on past best practies,
        and you will follow ALL of the rules below:

        1/ Response should be very similar or even identical to the past best practies,
        in terms of length, ton of voice, logical arguments and other details

        2/ If the best practice are irrelevant, then try to mimic the style of the best practice to prospect's message

        Below is a message I received from the prospect:
        {message}

        Here is a list of best practies of how we normally respond to prospect in similar scenarios:
        {best_practice}

        Please write the best response that I should send to this prospect:
        """

prompt = PromptTemplate(
    input_variables=["message", "best_practice"],
    template=template
)

chain = LLMChain(llm=llm, prompt=prompt)


# load DB from disk
# db = Chroma(persist_directory="chroma_db", embedding_function=embeddings)

# 2. Function for similarity search
def retrieve_info(query):
    # similar_response = db.similarity_search(query, k=1)
    similar_response = db.similarity_search(query)
    page_contents_array = [doc.page_content for doc in similar_response]
    return page_contents_array


# 4. Retrieval augmented generation
def generate_response(message):
    best_practice = retrieve_info(message)
    response = chain.run(message=message, best_practice=best_practice)
    return response


# 5. Build an app with streamlit
def main():
    app.run(debug=True, host="0.0.0.0", port=3000)
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
    result = generate_response(message)

    return jsonify({'output': result})

@app.route('/hello', methods=['GET'])
def basic():
    return jsonify({'output': "Martin jopa"})

@app.route('/join-meeting', methods=['GET'])
def join_meeting():
    role = request.args.get('meeting-id', type=str)
    print(os.getenv('SELENIUM_GMAIL'))
    print(os.getenv('SELENEUM_GPASSWORD'))
    AskToJoin(os.getenv('SELENIUM_GMAIL'), os.getenv('SELENEUM_GPASSWORD'))

    return jsonify({'output': "did we log in???"})


if __name__ == '__main__':
    main()
