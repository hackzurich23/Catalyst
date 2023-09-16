from data.transcripts import Meeting
from data.files_data import FileData
from faiss_db import FAISS_DB
from text2summary import Text2Summary
import os


def add_summaries_to_db(faiss_db: FAISS_DB, extractor: Text2Summary, meetings: list[Meeting]=[], file_data: list[FileData]=[]):
    """Populate the database with the summaries of the meetings and other files."""
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
        dir_path = os.path.dirname(os.path.realpath(__file__))

        with open(os.path.join(dir_path, meeting.transcript_path), "r") as f:
            text = f.read()
            q_and_a = extractor.get_meeting_summary(text)
            faiss_db.append_q_and_a_as_document(q_and_a, metadata=metadata)
            
    for fd in file_data:
        metadata = {
            "link": fd.file_link,
            "contacts": fd.department,
            "title": fd.product,
            "type": "file",
            "security_level_0": meeting.security_level_0,
            "security_level_1": meeting.security_level_1,
            "security_level_2": meeting.security_level_2,
        }
        with open(os.path.join(dir_path, fd.file_path), "r") as f:
            text = f.read()
            q_and_a = extractor.get_meeting_summary(text)
            faiss_db.append_q_and_a_as_document(q_and_a, metadata=metadata)
            