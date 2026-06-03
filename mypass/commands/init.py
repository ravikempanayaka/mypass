import os

from mypass.storage import FILE_PATH


def run():

    if FILE_PATH.exists():
        print("Vault already exists.")
        return

    FILE_PATH.touch()

    os.chmod(
        FILE_PATH,
        0o600
    )

    print(
        f"Created {FILE_PATH}"
    )