from mypass.storage import (
    MFA_FILE
)


def run():

    if MFA_FILE.exists():

        MFA_FILE.unlink()

        print(
            "MFA disabled."
        )

    else:

        print(
            "MFA is not enabled."
        )