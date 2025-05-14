from pathlib import Path

def write_file(file_name, file_content):
   path = Path(file_name).with_suffix('.txt')
   with path.open(mode="w", encoding="utf-8") as file:
     file.write(file_content)

def append_file(file_name, append_content):
    path = Path(file_name).with_suffix('.txt')
    with path.open(mode="a", encoding="utf-8") as file:
       file.write(append_content)

def read_file(file_name):
    path = Path(file_name).with_suffix('.txt')
    with path.open(mode="r", encoding="utf-8") as file:
        return file.read()
