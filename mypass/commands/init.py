from mypass.storage import get_file_path


def run():

    file_path = get_file_path()

    if file_path.exists():
        print(f"Already exists: {file_path}")
        return

    file_path.touch()

    print(f"Created: {file_path}")