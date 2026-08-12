
from src.file_organizer.scanner import scan_directory

files = scan_directory("examples")

for file in files:
    print("Archivo:", file.name, file.suffix, file.parent)