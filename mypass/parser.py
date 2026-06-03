from mypass.storage import FILE_PATH


def parse_mypass():

    if not FILE_PATH.exists():
        return {}

    data = {}

    current_section = None
    current_record = {}

    with open(FILE_PATH, "r") as file:

        for line in file:

            line = line.strip()

            if not line:

                if (
                    current_record
                    and current_section
                ):

                    data.setdefault(
                        current_section,
                        []
                    )

                    data[
                        current_section
                    ].append(
                        current_record
                    )

                    current_record = {}

                continue

            if (
                line.startswith("[")
                and line.endswith("]")
            ):

                current_section = (
                    line[1:-1]
                )

                continue

            if ":" in line:

                key, value = (
                    line.split(
                        ":",
                        1
                    )
                )

                current_record[
                    key.strip()
                ] = value.strip()

    if (
        current_record
        and current_section
    ):

        data.setdefault(
            current_section,
            []
        )

        data[
            current_section
        ].append(
            current_record
        )

    return data