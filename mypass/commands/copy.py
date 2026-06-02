import platform
import subprocess
import getpass

from mypass.parser import parse_mypass


def copy_to_clipboard(text):

    system = platform.system()

    try:

        if system == "Windows":

            subprocess.run(
                ["clip"],
                input=text.encode(),
                check=True,
                shell=True
            )

        elif system == "Darwin":

            subprocess.run(
                ["pbcopy"],
                input=text.encode(),
                check=True
            )

        else:

            try:
                subprocess.run(
                    ["xclip", "-selection", "clipboard"],
                    input=text.encode(),
                    check=True
                )

            except FileNotFoundError:

                subprocess.run(
                    ["xsel", "--clipboard", "--input"],
                    input=text.encode(),
                    check=True
                )

        return True

    except Exception as error:

        print(
            f"Clipboard copy failed: {error}"
        )

        return False


def run(keyword):

    keyword = keyword.lower()

    data = parse_mypass()

    for section, records in data.items():

        for record in records:

            values = [
                str(v).lower()
                for v in record.values()
            ]

            if (
                keyword in section.lower()
                or any(
                    keyword in value
                    for value in values
                )
            ):

                print("\nAvailable Fields\n")

                fields = list(record.keys())

                for index, field in enumerate(
                    fields,
                    start=1
                ):
                    print(
                        f"{index}. {field}"
                    )

                choice = input(
                    "\nSelect field to copy: "
                ).strip()

                try:

                    selected_field = (
                        fields[int(choice) - 1]
                    )

                except (
                    ValueError,
                    IndexError
                ):
                    print(
                        "Invalid selection"
                    )
                    return

                value = record[selected_field]

                if copy_to_clipboard(
                    value
                ):
                    print(
                        f"\n'{selected_field}' copied to clipboard."
                    )

                return

    print(
        f"No matching record found. {getpass.getuser()}"
    )