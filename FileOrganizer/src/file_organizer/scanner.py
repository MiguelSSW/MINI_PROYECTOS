
#Llama una libreria para escanear una carpeta y devolver una lista de archivos en ella.
from os import path
from pathlib import Path

# define la función scan_directory que toma un directorio como argumento y devuelve una lista de archivos en él.
def scan_directory(directory: str) -> list[Path]:
    path = Path(directory)
 
#realiza una busqueda para verificar si la ruta existe y si es un directorio. Si no es así, lanza una excepción.
    if not path.exists():
        raise FileNotFoundError(f"la carpeta no existe '{directory}' does not exist.")

    if not path.is_dir():
        raise NotADirectoryError(f"La ruta no es una carpeta '{directory}' is not a directory.")

    files: list[Path] = []

    for item in path.rglob("*"):
        if item.is_file():
            files.append(item)

    return files