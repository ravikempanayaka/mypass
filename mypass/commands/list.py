from mypass.parser import parse_mypass


def run():

    data = parse_mypass()

    if not data:
        print("No records found.")
        return

    print()

    for section, records in data.items():

        print(f"[{section}]")

        for record in records:

            name = record.get("Name", "")

            print(f"  - {name}")

        print()