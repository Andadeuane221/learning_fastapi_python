from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher

pwd_context = PasswordHash((Argon2Hasher(),))

def hash(password: str):
    return pwd_context.hash(password)