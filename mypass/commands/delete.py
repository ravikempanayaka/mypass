from mypass.parser import parse_mypass
from mypass.storage import get_file_path


def run(keyword):

    keyword = keyword.lower()

    data = parse_mypass()

    deleted = False

    file_path = get_file_path()

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as f:

        for section, records in data.items():

            for record in records:

                values = [
                    str(v).lower()
                    for v in record.values()
                ]

                if any(
                    keyword in value
                    for value in values
                ):
                    deleted = True
                    continue

                f.write(
                    f"\n[{section}]\n"
                )

                for key, value in record.items():
                    f.write(
                        f"{key}: {value}\n"
                    )

                f.write("\n")

    if deleted:
        print("Record deleted.")
    else:
        print("No record found.")