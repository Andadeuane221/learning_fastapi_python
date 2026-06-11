from fastapi import Depends, status, HTTPException, Response, APIRouter
from sqlalchemy import select
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas, utils

router = APIRouter(
	prefix="/users",
	tags=['Users']
)

@router.get("/", response_model=list[schemas.UserPublic])
def get_users(db: Session = Depends(get_db)):
	stmt = select(models.User)
	users = db.execute(stmt).scalars().all()
	return users

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserPublic)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
	hashed_password = utils.hash(user.password)
	user.password = hashed_password
	new_user = models.User(**user.model_dump())
	db.add(new_user)
	db.commit()
	db.refresh(new_user)
	return new_user

@router.get("/{id}", response_model=schemas.UserPublic)
def get_user(id: int, db: Session = Depends(get_db)):
	stmt = select(models.User).where(models.User.id == id)
	user = db.scalars(stmt).first()
	if not user:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} was not found")
	return user

@router.put("/{id}", response_model=schemas.UserPublic)
def update_user(id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
	stmt = select(models.User).where(models.User.id == id)
	user_query = db.scalars(stmt).first()
	if not user_query:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} does not exist")
	user_query.name = user.name
	user_query.email = user.email
	hashed_password = utils.hash(user.password)
	user.password = hashed_password
	user_query.password = user.password
	db.commit()
	db.refresh(user_query)
	return user_query

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(id: int, db: Session = Depends(get_db)):
	stmt = select(models.User).where(models.User.id == id)
	user_to_delete = db.scalars(stmt).first()
	if not user_to_delete:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id: {id} does not exist")
	db.delete(user_to_delete)
	db.commit()
	return Response(status_code=status.HTTP_204_NO_CONTENT)