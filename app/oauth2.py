from datetime import datetime, timedelta, timezone
import jwt
from jwt.exceptions import InvalidTokenError

SECRET_KEY = "9d9e2c2847be04e4a11ba103fd91a75517e4ee2286b1ab6aac7b2ec603c0de1d"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
	to_enconde = data.copy()
	expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
	to_enconde.update({"exp": expire})
	encoded_jwt = jwt.encode(to_enconde, SECRET_KEY, algorithm=ALGORITHM)
	return encoded_jwt