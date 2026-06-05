def encrypt(text, cipher):

    return (
        "ENC:"
        + cipher.encrypt(
            text.encode()
        ).decode()
    )


def decrypt(text, cipher):

    if not text.startswith(
        "ENC:"
    ):
        return text

    return cipher.decrypt(
        text[4:].encode()
    ).decode()