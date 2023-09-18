from dataclasses import dataclass, field


# Hardcode the transcriptions of the recorded meetings here for now. 
# We use google's speech-to-text API to generate the transcripts automatically.
# TODO: Use the Google Drive API to access the transcripts directly from the google drive folder.

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
    

@dataclass
class FileData:
    file_path: str
    file_link: str
    product: str = "No title"
    department: str = "No meeting id"
    security_level_0: bool = True       # Who has access 
    security_level_1: bool = True
    security_level_2: bool = True

    
ALL_MEETINGS = [
    # Meeting(
    #     participants=["John Cena", "Jane", "Spoderman"],
    #     transcript_path="data/all_transcripts/kmk-wovu-mzz (2023-09-16 08_30 GMT) - Transcript.txt",
    #     transcript_link="https://docs.google.com/document/d/1zCIHmP6lrKfTaMvZmKiZEivl3CBGtcBdBg3Ob3-sa4c/edit?usp=sharing"
    # ),
]


ALL_FILES = [
    FileData(
        file_path="data/files_data/3D CONCRETE PRINTING.txt",
        file_link="https://usa.sika.com/en/construction/concrete/3d-concrete-printing.html",
        product="3D CONCRETE PRINTING",
        department="Construction",
    ),
    FileData(
        file_path="data/files_data/Waterproofing.txt",
        file_link="https://usa.sika.com/en/construction/floor-covering/tile-stone-installation/waterproofing.html",
        product="Waterproofing",
        department="Construction",
    ),
    FileData(
        file_path="data/files_data/Grout (Tiles).txt",
        file_link="https://usa.sika.com/en/construction/floor-covering/tile-stone-installation/grouts.html",
        product="Grout",
        department="Construction",
    ),
    FileData(
        file_path="data/files_data/Anchor Fix Adhesive.txt",
        file_link="https://usa.sika.com/content/dam/dms/us01/t/sika_anchorfix_-1.pdf",
        product="Grout",
        department="Adhesives",
    ),
    FileData(
        file_path="data/files_data/CarboDur Rods",
        file_link="https://usa.sika.com/content/dam/dms/us01/b/sika_carbodur_rods.pdf",
        product="CarboDur Rods",
        department="Construction",
    ),
    FileData(
        file_path="data/files_data/FAQ",
        file_link="https://usa.sika.com/en/industry/resource-center/faq.html",
        product="FAQ",
        department="Construction",
    ),
    FileData(
        file_path="data/files_data/ipd-pds-sikaflex 124-us.txt",
        file_link="https://usa.sika.com/content/dam/dms/us01/b/sika_carbodur_rods.pdf",
        product="sikaflex-124",
        department="Construction",
    ),
    FileData(
        file_path="data/files_data/ipd-pds-sikaflex265-us.txt",
        file_link="https://usa.sika.com/content/dam/dms/us01/2/ipd-pds-sikaflex265-us.pdf",
        product="sikaflex-265",
        department="Construction",
    ),
    FileData(
        file_path="data/files_data/ipd-pds-sikalastomer-65-us.txt",
        file_link="https://usa.sika.com/content/dam/dms/us01/4/ipd-pds-sikalastomer-65-us.pdf",
        product="sikalastomer",
        department="Construction",
    ),
    FileData(
        file_path="data/files_data/SikaBiresin AP112 PDS.txt",
        file_link="https://usa.sika.com/content/dam/dms/us01/o/SikaBiresin%20AP112%20PDS.pdf",
        product="SikaBiresin",
        department="Construction",
    ),
    FileData(
        file_path="data/files_data/sikaflex-221.txt",
        file_link="https://usa.sika.com/content/dam/dms/us01/b/sika_carbodur_rods.pdf",
        product="sikaflex-221",
        department="Construction",
    ),
    FileData(
        file_path="data/files_data/sikaflex_-296.txt",
        file_link="https://usa.sika.com/content/dam/dms/us01/c/sikaflex_-296.pdf",
        product="sikaflex-296",
        department="Construction",
    ),
]