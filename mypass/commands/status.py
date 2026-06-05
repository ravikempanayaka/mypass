from mypass.session import (
    is_session_valid,
    get_remaining_minutes
)


def run():

    if not is_session_valid():

        print(
            "Vault: Locked"
        )

        return

    print(
        "Vault: Unlocked"
    )

    print(
        f"Expires in: "
        f"{get_remaining_minutes()} "
        f"minutes"
    )