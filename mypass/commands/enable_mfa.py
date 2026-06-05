import pyotp
import qrcode

from mypass.mfa import (
    save_secret
)
from mypass.security import (
    verify_master_password
)


def choose_authenticator():

    print(
        "\nSelect Authenticator\n"
    )

    print(
        "1. Microsoft Authenticator"
    )

    print(
        "2. Google Authenticator"
    )

    choice = input(
        "\nChoice: "
    ).strip()

    if choice == "1":

        print(
            "\nMicrosoft Authenticator Setup"
        )

        print(
            "1. Open Microsoft Authenticator"
        )

        print(
            "2. Click '+'"
        )

        print(
            "3. Select 'Other Account'"
        )

        print(
            "4. Scan QR Code\n"
        )

        return "Microsoft Authenticator"

    print(
        "\nGoogle Authenticator Setup"
    )

    print(
        "1. Open Google Authenticator"
    )

    print(
        "2. Click '+'"
    )

    print(
        "3. Scan QR Code\n"
    )

    return "Google Authenticator"


def display_qr(uri):

    qr = qrcode.QRCode()

    qr.add_data(uri)

    qr.make()

    qr.print_ascii(
        invert=True
    )


def run():

    choose_authenticator()

    secret = (
        pyotp.random_base32()
    )

    uri = (
        pyotp.TOTP(secret)
        .provisioning_uri(
            name="SecureMyPass",
            issuer_name="Secure MyPass"
        )
    )

    print(
        "\nScan QR Code Below\n"
    )

    display_qr(uri)

    totp = pyotp.TOTP(
        secret
    )

    otp = input(
        "\nEnter OTP to verify setup: "
    ).strip()

    if not totp.verify(
        otp
    ):

        print(
            "\nInvalid OTP."
        )

        return

    cipher = (
        verify_master_password()
    )

    if not cipher:
        return

    save_secret(
        secret,
        cipher
    )

    print(
        "\n✓ MFA enabled successfully."
    )