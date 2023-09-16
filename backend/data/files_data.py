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
]