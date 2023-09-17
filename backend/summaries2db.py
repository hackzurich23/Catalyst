from data.all_files import Meeting, FileData
from faiss_db import FAISS_DB
from text2summary import Text2Summary
import os


def add_summaries_to_db(faiss_db: FAISS_DB, extractor: Text2Summary, meetings: list[Meeting]=[], file_data: list[FileData]=[], type="q&a"):
    """Populate the database with the summaries of the meetings and other files."""
    dir_path = os.path.dirname(os.path.realpath(__file__))

    for meeting in meetings:
        metadata = {
            "link": meeting.transcript_link,
            "contacts": meeting.participants,
            "title": meeting.title,
            "type": "meeting",
            "security_level_0": meeting.security_level_0,
            "security_level_1": meeting.security_level_1,
            "security_level_2": meeting.security_level_2,
        }
        with open(os.path.join(dir_path, meeting.transcript_path), "r") as f:
            text = f.read()
            print(f"Embedding meeting transcript: {meeting.title}")
            q_and_a = extractor.get_meeting_summary(text, type=type)
            if type == "q&a":
                faiss_db.append_q_and_a_as_document(q_and_a, metadata=metadata)
            else:
                faiss_db.append_fact_as_document(q_and_a, metadata=metadata)
    for fd in file_data:
        metadata = {
            "link": fd.file_link,
            "contacts": fd.department,
            "title": fd.product,
            "type": "file",
            "security_level_0": fd.security_level_0,
            "security_level_1": fd.security_level_1,
            "security_level_2": fd.security_level_2,
        }
        with open(os.path.join(dir_path, fd.file_path), "r") as f:
            text = f.read()
            print(f"Embedding file: {fd.product}")
            q_and_a = extractor.get_document_summary(text, type=type)
            if type == "q&a":
                faiss_db.append_q_and_a_as_document(q_and_a, metadata=metadata)
            else:
                faiss_db.append_fact_as_document(q_and_a, metadata=metadata)
            