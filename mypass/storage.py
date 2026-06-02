from pathlib import Path

FILE_PATH = Path.home() / ".mypass"


def get_file_path():
    return FILE_PATH