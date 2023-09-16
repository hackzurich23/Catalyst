from dotenv import load_dotenv
from flask import Flask, request, jsonify
import os
from meeting_participant import launch_bot
from faiss_db import FAISS_DB
from data.transcripts import ALL_MEETINGS
from llm import LLM
from text2summary import Text2Summary
from summaries2db import add_summaries_to_db
import re
import json


# Define global variables:
app = Flask(__name__)
load_dotenv()

# Create the vector database and the langchain model
faiss_db = FAISS_DB()
educated_llm = LLM()

# Add the transcripts to the DB
extractor = Text2Summary()
if not os.path.exists("faiss_index"):
    add_summaries_to_db(faiss_db, extractor, ALL_MEETINGS)
    faiss_db.save_to_disk()

def main():
    app.run(debug=True, host="0.0.0.0", port=3000)

#     FLASK ROUTES
@app.route('/task', methods=['GET'])
def calculate_task():
    # Get the query parameters
    role = request.args.get('role', type=str)
    task_type = request.args.get('task_type', type=str)
    message = request.args.get('message', type=str)
    # TODO: define DB depending on the user's role and define prompt depending on the task_type
    response, education, metadata, scores = educated_llm.get_educated_response(faiss_db, message)
    
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
        "scores": json.dumps(str(scores)),
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
