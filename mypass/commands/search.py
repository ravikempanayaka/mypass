from mypass.parser import parse_mypass

SENSITIVE_FIELDS = {
    "password",
    "token",
    "secret",
    "api_key",
    "recovery_codes",
    "app password",
    "app token",
    "app secret",
    "apppassword",
    "app_password",
    "systempassword"
    "system_sassword"
}


def run(keyword):

    keyword = keyword.lower()

    data = parse_mypass()

    found = False

    for section, records in data.items():

        for record in records:

            section_match = (
                keyword in section.lower()
            )

            record_match = any(
                keyword in str(value).lower()
                for value in record.values()
                if not str(value).startswith("ENC:")
            )

            if section_match or record_match:

                found = True

                print(f"\n[{section}]")

                for key, value in record.items():

                    if (
                        key.lower()
                        in SENSITIVE_FIELDS
                    ):
                        print(
                            f"{key}: ********"
                        )
                    else:
                        print(
                            f"{key}: {value}"
                        )

    if not found:
        print(
            f"No matching records found for '{keyword}'."
        )