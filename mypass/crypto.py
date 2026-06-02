from cryptography.fernet import Fernet
from hashlib import sha256
import base64


def generate_key(master_password: str):
    digest = sha256(master_password.encode()).digest()
    return base64.urlsafe_b64encode(digest)


def encrypt(value: str, master_password: str):
    key = generate_key(master_password)
    return Fernet(key).encrypt(value.encode()).decode()


def decrypt(value: str, master_password: str):
    key = generate_key(master_password)
    return Fernet(key).decrypt(value.encode()).decode()