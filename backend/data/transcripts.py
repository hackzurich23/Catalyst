from dataclasses import dataclass, field

@dataclass
class Meeting:
    transcript_path: str
    transcript_link: str
    title: str = "No title"
    meeting_id: str = "No meeting id"
    participants: list[str] = field(default_factory=lambda: ["John Doe", "Jane Doe"])
    security_level_0: bool = True       # Who has access to this meeting
    security_level_1: bool = True
    security_level_2: bool = True

    
ALL_MEETINGS = [
    Meeting(
        participants=["John Cena", "Jane", "Spoderman"],
        transcript_path="data/all_transcripts/kmk-wovu-mzz (2023-09-16 08_30 GMT) - Transcript.txt",
        transcript_link="https://docs.google.com/document/d/1zCIHmP6lrKfTaMvZmKiZEivl3CBGtcBdBg3Ob3-sa4c/edit?usp=sharing"
    ),
]