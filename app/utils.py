from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher

pwd_context = PasswordHash((Argon2Hasher(),))

def hash(password: str):
	return pwd_context.hash(password)

def verify(plain_pwd, hashed_pwd):
	return (pwd_context.verify(plain_pwd, hashed_pwd))