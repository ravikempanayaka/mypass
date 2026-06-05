import json
import time

from mypass.storage import (
    SESSION_FILE
)

SESSION_TIMEOUT = 90


def create_session():

    expires_at = (
        int(time.time())
        + SESSION_TIMEOUT
    )

    SESSION_FILE.write_text(
        json.dumps(
            {
                "expires_at": expires_at
            }
        )
    )

    try:
        SESSION_FILE.chmod(0o600)
    except Exception:
        pass


def is_session_valid():

    if not SESSION_FILE.exists():
        return False

    try:

        data = json.loads(
            SESSION_FILE.read_text()
        )

        expires_at = data.get(
            "expires_at",
            0
        )

        return (
            time.time()
            < expires_at
        )

    except Exception:

        return False


def get_remaining_minutes():

    if not is_session_valid():
        return 0

    data = json.loads(
        SESSION_FILE.read_text()
    )

    remaining = (
        data["expires_at"]
        - time.time()
    )

    return int(
        remaining / 60
    )


def clear_session():

    if SESSION_FILE.exists():

        SESSION_FILE.unlink()