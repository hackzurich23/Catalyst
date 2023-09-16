from data.transcripts import Meeting
from faiss_db import FAISS_DB
from text2summary import Text2Summary


def add_summaries_to_db(faiss_db: FAISS_DB, extractor: Text2Summary, meetings: list[Meeting]):
    
    for meeting in meetings:
        metadata = {
            "link": meeting.transcript_link,
            "contacts": meeting.participants,
        }
        with open(meeting.transcript_path, "r") as f:
            text = f.read()
            q_and_a = extractor.get_meeting_summary(text)
            faiss_db.append_q_and_a_as_document(q_and_a, metadata=metadata)
            