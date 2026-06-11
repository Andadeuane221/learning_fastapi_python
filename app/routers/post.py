from fastapi import Depends, status, HTTPException, Response, APIRouter
from sqlalchemy import select
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models, schemas

router = APIRouter(
	prefix="/posts",
	tags=['Posts']
)

@router.get("/", response_model=list[schemas.Post])
def get_posts(db: Session = Depends(get_db)):
	stmt = select(models.Post)
	posts = db.execute(stmt).scalars().all()
	return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db)):
	new_post = models.Post(**post.model_dump())
	db.add(new_post)
	db.commit()
	db.refresh(new_post)
	return new_post

@router.get("/{id}", response_model=schemas.Post)
def get_post(id: int, db: Session = Depends(get_db)):
	stmt = select(models.Post).where(models.Post.id == id)
	post = db.scalars(stmt).first()
	if not post:
		raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
	return post

@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, post: schemas.PostCreate, db: Session = Depends(get_db)):
	stmt = select(models.Post).where(models.Post.id == id)
	post_query = db.scalars(stmt).first()
	if not post_query:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
	post_query.title = post.title
	post_query.content = post.content
	post_query.published = post.published
	db.commit()
	db.refresh(post_query)
	return post_query

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
	stmt = select(models.Post).where(models.Post.id == id)
	post_to_delete = db.scalars(stmt).first()
	if not post_to_delete:
		raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
	db.delete(post_to_delete)
	db.commit()
	return Response(status_code=status.HTTP_204_NO_CONTENT)

