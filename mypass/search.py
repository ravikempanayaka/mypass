from mypass.parser import parse_mypass


def search(keyword):

    keyword = keyword.lower()

    data = parse_mypass()

    found = False

    for section, records in data.items():

        for record in records:

            values = [
                str(value).lower()
                for value in record.values()
            ]

            if (
                keyword in section.lower()
                or any(keyword in value for value in values)
            ):

                found = True

                print(f"\n[{section}]")

                for key, value in record.items():
                    print(f"{key}: {value}")

    if not found:
        print("No matching records found.")