from dataclasses import dataclass, field

@dataclass
class FileData:
    file_path: str
    file_link: str
    product: str = "No title"
    department: str = "No meeting id"

    
ALL_Files = [
    FileData(
        file_path="data/files_data/3D CONCRETE PRINTING.txt",
        file_link="https://usa.sika.com/en/construction/concrete/3d-concrete-printing.html",
        product="3D CONCRETE PRINTING",
        department="Construction",
    ),
]