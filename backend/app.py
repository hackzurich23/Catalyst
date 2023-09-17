from dotenv import load_dotenv
from flask import Flask, request, jsonify
import os
from meeting_participant import launch_bot
from faiss_db import FAISS_DB
from data.all_files import ALL_MEETINGS, ALL_FILES
from llm import LLM
from text2summary import Text2Summary
from summaries2db import add_summaries_to_db
import re
import json
from PyPDF2 import PdfReader


# Define global variables:
app = Flask(__name__)
load_dotenv()

# Create the vector database and the langchain model
faiss_db = FAISS_DB()
educated_llm = LLM()

# Add the transcripts to the DB
extractor = Text2Summary()
if not os.path.exists("faiss_index"):
    add_summaries_to_db(faiss_db, extractor, ALL_MEETINGS, ALL_FILES)
    faiss_db.save_to_disk()

def main():
    app.run(debug=True, host="0.0.0.0", port=8080)

# FLASK ROUTES
@app.route('/task', methods=['GET'])
def calculate_task():
    # Get the query parameters
    role = request.args.get('role', type=str)
    task_type = request.args.get('task_type', type=str)
    message = request.args.get('message', type=str)
    # TODO: define DB depending on the user's role and define prompt depending on the task_type
    response, education, metadata, scores = educated_llm.get_educated_response(faiss_db, message, top_k=3)
    
    # Extract the questions and answers from the education strings.
    questions = []
    answers = []
    for item in education:
        question_match = re.search(r'question: (.*?)\n', item)
        answer_match = re.search(r'"answer": "(.*?)"', item)
        questions.append(question_match.group(1))
        answers.append(answer_match.group(1))
    
    # Build the output to the frontend.
    json_ret = jsonify({
        'output': response,
        "questions": questions,
        "answers": answers,
        "scores": [str(1-_) for _ in scores],
        "links": [_["link"] for _ in metadata],
        "contacts": [_["contacts"] for _ in metadata],
        "type": [_["type"] for _ in metadata],
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


# Add an endpoint for uploading a new pdf file
@app.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    # Get the file from the request
    file = request.files['file']
    # Save the file to the disk
    file_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "pdfs", file.filename)
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    file.save(file_path)
    # Extract the text from the pdf.
    reader = PdfReader(file_path)  
    full_text = ""
    for page in reader.pages:
        full_text += f"\n{page.extract_text()}"
    # Extract the summary from the text.
    extractor = Text2Summary()
    summary_q_and_a = extractor.get_document_summary(full_text)
    # Add the summary to the DB.
    faiss_db.append_q_and_a_as_document(
        summary_q_and_a,
        metadata={
            "type": "file", 
            "title": file.filename,
            "department": "Uploaded Document",
            "product": "Uploaded Document",
            "security_level_0": True,
            "security_level_1": True,
            "security_level_2": True,
        }
    )
    faiss_db.save_to_disk()
    
    return jsonify({'output': "Upload successful!"})


if __name__ == '__main__':
    main()
