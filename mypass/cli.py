import sys

from mypass.storage import get_file_path
from mypass.search import search


SAMPLE_CONTENT = """
[SSO Login]
Name: Portal SSO
Url: https://example.com
UserName: username
Password: password

[Email]
Name: Work Email
Email: user@example.com
Password: password
""".strip()


def initialize():

    file_path = get_file_path()

    if file_path.exists():
        print(f"Already exists: {file_path}")
        return

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(SAMPLE_CONTENT)

    print(f"Created: {file_path}")


def main():

    if len(sys.argv) < 2:
        print("Usage:")
        print("  mypass init")
        print("  mypass <keyword>")
        return

    command = sys.argv[1]

    if command == "init":
        initialize()
        return

    search(command)


if __name__ == "__main__":
    main()