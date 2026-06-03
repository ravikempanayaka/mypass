from mypass.parser import parse_mypass

from mypass.security import (
    verify_master_password,
    decrypt,
)


def run(keyword):

    keyword = keyword.lower()

    cipher = (
        verify_master_password()
    )

    if not cipher:
        return

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

                    try:

                        if (
                            isinstance(value, str)
                            and value.startswith("ENC:")
                        ):
                            value = decrypt(
                                value,
                                cipher
                            )

                    except Exception:
                        value = (
                            "<unable to decrypt>"
                        )

                    print(
                        f"{key}: {value}"
                    )

    if not found:

        print(
            f"No credential found for '{keyword}'."
        )