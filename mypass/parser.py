from mypass.storage import get_file_path


def parse_mypass():
    file_path = get_file_path()

    if not file_path.exists():
        return {}

    data = {}
    current_section = None
    current_record = {}

    with open(file_path, "r", encoding="utf-8") as f:

        for line in f:
            line = line.strip()

            if not line:

                if current_record and current_section:
                    data[current_section].append(current_record)
                    current_record = {}

                continue

            if line.startswith("[") and line.endswith("]"):

                current_section = line[1:-1]

                if current_section not in data:
                    data[current_section] = []

                continue

            if ":" in line:
                key, value = line.split(":", 1)

                current_record[key.strip()] = value.strip()

    if current_record and current_section:
        data[current_section].append(current_record)

    return data