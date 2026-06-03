from mypass.parser import (
    parse_mypass
)


def run():

    data = parse_mypass()

    for section, records in (
        data.items()
    ):

        print(
            f"\n[{section}]"
        )

        for record in records:

            print(
                "-",
                record.get(
                    "Name",
                    "Unknown"
                )
            )