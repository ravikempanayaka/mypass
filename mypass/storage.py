from pathlib import Path

FILE_PATH = Path.home() / ".mypass"
KEY_FILE = Path.home() / ".mypass.key"
MFA_FILE = Path.home() / ".mypass.mfa"
SESSION_FILE = Path.home() / ".mypass.session"


def get_file_path():
    return FILE_PATH