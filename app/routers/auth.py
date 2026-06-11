from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy import select
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils

router = APIRouter(tags=['Authentication'])

@router.post("/login")
def login(user_credentials: schemas.UserLogin, db: Session = Depends(database.get_db)):
	stmt = select(models.User).where(models.User.email == user_credentials.email)
	user_query = db.scalars(stmt).first()
	if not user_query:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
	if not utils.verify(user_credentials.password, user_query.password):
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid credentials")
	#create token
	#return token
	return {"token": "example token"}