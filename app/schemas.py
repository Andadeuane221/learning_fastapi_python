from pydantic import BaseModel, EmailStr
from datetime import datetime

# ==== POST SCHEMAS ====

class PostBase(BaseModel):
	title: str
	content: str
	published: bool = True

class PostCreate(PostBase):
	pass

class Post(PostBase):
	id: int
	created_at: datetime

# ==== USER SCHEMAS ====

class UserCreate(BaseModel):
	name: str
	email: EmailStr
	password: str

class UserPublic(BaseModel):
	id: int
	name: str
	email: EmailStr
	created_at: datetime

class UserLogin(BaseModel):
	email: EmailStr
	password: str

# ==== TOKEN SCHEMAS ====

class Token(BaseModel):
	access_token: str
	token_type: str

class TokenData(BaseModel):
	id: int | None = None
