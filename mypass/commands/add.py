import getpass

from mypass.parser import parse_mypass
from mypass.storage import get_file_path


SENSITIVE_FIELDS = {
    "password",
    "token",
    "secret",
    "secret_key",
    "api_key",
    "access_key",
    "recovery_code",
    "recovery_codes",
}


def select_section():
    data = parse_mypass()

    sections = list(data.keys())

    print("\nAvailable Sections\n")

    if sections:
        for index, section in enumerate(sections, start=1):
            print(f"{index}. {section}")

    print("0. Create New Section")

    choice = input("\nSelect section: ").strip()

    if choice == "0":
        return input(
            "Enter new section name: "
        ).strip()

    try:
        return sections[int(choice) - 1]

    except (ValueError, IndexError):
        print("Invalid selection")
        return None


def collect_fields():
    fields = {}

    print(
        "\nAdd fields (leave field name blank to finish)\n"
    )

    while True:

        field_name = input(
            "Field Name: "
        ).strip()

        if not field_name:
            break

        if field_name.lower() in SENSITIVE_FIELDS:

            value = getpass.getpass(
                f"{field_name}: "
            )

        else:

            value = input(
                f"{field_name}: "
            ).strip()

        fields[field_name] = value

    return fields


def save_record(section, fields):

    file_path = get_file_path()

    with open(
        file_path,
        "a",
        encoding="utf-8"
    ) as file:

        file.write(f"\n\n[{section}]\n")

        for key, value in fields.items():
            file.write(
                f"{key}: {value}\n"
            )


def run():

    section = select_section()

    if not section:
        return

    print(
        f"\nUsing Section: {section}"
    )

    fields = collect_fields()

    if not fields:
        print(
            "No fields entered."
        )
        return

    save_record(
        section=section,
        fields=fields
    )

    print(
        "\nCredential added successfully."
    )