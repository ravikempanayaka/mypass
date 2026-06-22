from mypass.parser import parse_mypass
from mypass.security import authenticate
from mypass.storage import FILE_PATH


def run(keyword):
    cipher = authenticate()

    if not cipher:
        return

    keyword = keyword.lower()

    data = parse_mypass()

    found = False

    target_section = None
    target_record = None

    for section, records in data.items():

        for record in records:

            section_match = (
                    keyword in section.lower()
            )

            record_match = any(
                keyword in str(value).lower()
                for value in record.values()
            )

            if section_match or record_match:

                found = True

                target_section = section
                target_record = record

                print(
                    f"\n[{section}]"
                )

                for key, value in record.items():

                    if str(value).startswith("ENC:"):
                        value = "********"

                    print(
                        f"{key}: {value}"
                    )

                break

        if found:
            break

    if not found:
        print(
            f"No credential found for '{keyword}'."
        )

        return

    confirm = input(
        "\nDelete this credential? (y/n): "
    ).strip().lower()

    if confirm != "y":
        print(
            "Delete cancelled."
        )

        return

    data[target_section].remove(
        target_record
    )

    save_data(data)

    print(
        "Credential deleted successfully."
    )


def save_data(data):
    with open(
            FILE_PATH,
            "w",
            encoding="utf-8"
    ) as file:

        first_section = True

        for section, records in data.items():

            for record in records:

                if not first_section:
                    file.write("\n")

                first_section = False

                file.write(
                    f"[{section}]\n"
                )

                for key, value in record.items():
                    file.write(
                        f"{key}: {value}\n"
                    )

                file.write("\n")
