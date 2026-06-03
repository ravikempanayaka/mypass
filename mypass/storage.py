from pathlib import Path

FILE_PATH = Path.home() / ".mypass"
KEY_FILE = Path.home() / ".mypass.key"


def get_file_path():
    return FILE_PATH