import os
import json
import base64
import getpass

from hashlib import pbkdf2_hmac
from cryptography.fernet import Fernet

from mypass.storage import KEY_FILE
VERIFY_TEXT = "SECURE_MYPASS_VERIFICATION"
from mypass.session import (
    is_session_valid,
    create_session
)

from mypass.crypto_utils import (
    encrypt,
    decrypt
)

def verify_master_password():

    if not KEY_FILE.exists():

        print(
            "Master password not configured."
        )

        print(
            "Run: mypass setup"
        )

        return None

    password = getpass.getpass(
        "Master Password: "
    )

    try:

        cipher = get_cipher(
            password
        )

        data = json.loads(
            KEY_FILE.read_text()
        )

        verify_token = data.get(
            "verify"
        )

        if not verify_token:

            print(
                "Master password verification not configured."
            )

            return None

        decrypted = (
            cipher.decrypt(
                verify_token.encode()
            ).decode()
        )

        if decrypted != "SECURE_MYPASS_VERIFICATION":

            print(
                "Invalid master password."
            )

            return None

        return cipher

    except Exception:

        print(
            "Invalid master password."
        )

        return None

def setup_master_password():

    if KEY_FILE.exists():
        print(
            "Master password already configured."
        )
        return

    password = getpass.getpass(
        "Create Master Password: "
    )

    confirm = getpass.getpass(
        "Confirm Master Password: "
    )

    if password != confirm:
        print(
            "Passwords do not match."
        )
        return

    salt = os.urandom(16)

    # Create temporary key file
    KEY_FILE.write_text(
        json.dumps(
            {
                "salt": base64.b64encode(
                    salt
                ).decode()
            }
        )
    )

    cipher = get_cipher(password)

    verify_token = cipher.encrypt(
        VERIFY_TEXT.encode()
    ).decode()

    KEY_FILE.write_text(
        json.dumps(
            {
                "salt": base64.b64encode(
                    salt
                ).decode(),
                "verify": verify_token
            }
        )
    )

    KEY_FILE.chmod(0o600)

    print(
        "Master password configured."
    )


def get_cipher(master_password):

    data = json.loads(
        KEY_FILE.read_text()
    )

    salt = base64.b64decode(
        data["salt"]
    )

    key = pbkdf2_hmac(
        "sha256",
        master_password.encode(),
        salt,
        600000,
        dklen=32
    )

    key = base64.urlsafe_b64encode(
        key
    )

    return Fernet(key)


def prompt_cipher():

    password = getpass.getpass(
        "Master Password: "
    )

    return get_cipher(password)


def encrypt(text, cipher):

    return (
        "ENC:"
        + cipher.encrypt(
            text.encode()
        ).decode()
    )


def decrypt(text, cipher):

    if not text.startswith("ENC:"):
        return text

    encrypted = text[4:]

    return cipher.decrypt(
        encrypted.encode()
    ).decode()

def authenticate():

    if is_session_valid():

        return prompt_cipher()

    cipher = verify_master_password()

    if not cipher:
        return None

    from mypass.mfa import verify

    if not verify(cipher):

        print(
            "Invalid OTP."
        )

        return None

    create_session()

    return cipher