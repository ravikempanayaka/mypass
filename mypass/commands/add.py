import getpass

from mypass.parser import (
    parse_mypass
)
from mypass.security import (
    verify_master_password,
    encrypt,
)
from mypass.storage import (
    FILE_PATH
)
from mypass.mfa import verify
from mypass.security import (
        authenticate
    )

SENSITIVE_FIELDS = {
    "password",
    "token",
    "secret",
    "api_key",
    "recovery_codes",
    "apppassword",
    "app_password",
    "systemsassword"
    "system_password"

}


def run():
    cipher = authenticate()


    if not cipher:
        return

    # if not verify():
    #     print(
    #         "Invalid OTP."
    #     )
    #
    #     return

    data = parse_mypass()

    sections = list(data.keys())

    print("\nSections\n")

    for index, section in enumerate(
            sections,
            start=1
    ):
        print(
            f"{index}. {section}"
        )

    print("0. New Section")

    choice = input(
        "\nSelect: "
    ).strip()

    if choice == "0":

        section = input(
            "Section Name: "
        ).strip()

    else:

        try:

            section = sections[
                int(choice) - 1
                ]

        except (
                ValueError,
                IndexError
        ):

            print(
                "Invalid selection."
            )

            return

    fields = {}

    while True:

        key = input(
            "Field Name: "
        ).strip()

        if not key:
            break

        if (
                key.lower()
                in SENSITIVE_FIELDS
        ):

            value = (
                getpass.getpass(
                    f"{key}: "
                )
            )

            value = encrypt(
                value,
                cipher
            )

        else:

            value = input(
                f"{key}: "
            ).strip()

        fields[key] = value

    with open(
            FILE_PATH,
            "a",
            encoding="utf-8"
    ) as file:

        file.write(
            f"\n\n[{section}]\n"
        )

        for key, value in (
                fields.items()
        ):
            file.write(
                f"{key}: {value}\n"
            )

    print(
        "\nCredential added successfully."
    )
