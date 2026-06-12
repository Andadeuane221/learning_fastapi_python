from datetime import datetime, timedelta, timezone
import jwt
from jwt.exceptions import InvalidTokenError
from . import schemas, database, models
import os
from dotenv import load_dotenv
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.orm import Session

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict):
	to_enconde = data.copy()
	expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
	to_enconde.update({"exp": expire})
	encoded_jwt = jwt.encode(to_enconde, SECRET_KEY, algorithm=ALGORITHM)
	return encoded_jwt

def verify_access_token(token: str, credentials_exception):
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		_id = payload.get("user_id")
		if _id is None:
			raise credentials_exception
		token_data = schemas.TokenData(id=_id)
	except InvalidTokenError:
		raise credentials_exception
	return token_data

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
	credentials_exception = HTTPException(
		status_code=status.HTTP_401_UNAUTHORIZED,
		detail="Could not validate credentials",
		headers={"WWW-Authenticate": "Bearer"})
	token_data = verify_access_token(token, credentials_exception)
	stmt = select(models.User).where(models.User.id == token_data.id)
	user = db.scalars(stmt).first()
	if not user:
		raise credentials_exception
	return user
