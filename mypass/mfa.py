import json
import pyotp

from mypass.storage import (
    MFA_FILE
)

from mypass.crypto_utils import (
    encrypt,
    decrypt
)


def save_secret(
    secret,
    cipher
):

    encrypted_secret = encrypt(
        secret,
        cipher
    )

    MFA_FILE.write_text(
        json.dumps(
            {
                "secret": encrypted_secret
            }
        )
    )


def get_secret(
    cipher
):

    data = json.loads(
        MFA_FILE.read_text()
    )

    encrypted_secret = (
        data["secret"]
    )

    return decrypt(
        encrypted_secret,
        cipher
    )


def verify(
    cipher
):

    if not MFA_FILE.exists():
        print(
            "\nMFA is not configured."
        )

        print(
            "Run: mypass enable-mfa"
        )
        return True

    secret = get_secret(
        cipher
    )

    otp = input(
        "OTP: "
    ).strip()

    totp = pyotp.TOTP(
        secret
    )

    return totp.verify(
        otp
    )