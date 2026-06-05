import os
import time
import psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv
from fastapi import FastAPI, status, HTTPException, Response
from pydantic import BaseModel
from . import models
from .database import engine, get_db
from sqlalchemy import select, insert
from sqlalchemy.orm import Session
from fastapi import Depends

models.Base.metadata.create_all(engine)

load_dotenv()

db_password = os.getenv("DB_PASSWORD")
db_user = os.getenv("DB_USER")
db_name = os.getenv("DB_NAME")

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

@app.get("/")
async def root():
    return {"message": "welcome to my api!!!"}

@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    stmt = select(models.Post)
    posts = db.execute(stmt).scalars().all()
    return {"data": posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post, db: Session = Depends(get_db)):
    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"data": new_post}

@app.get("/posts/{id}")
def get_post(id: int, db: Session = Depends(get_db)):
    stmt = select(models.Post).where(models.Post.id == id)
    post = db.scalars(stmt).first()
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return {"post_detail": post}

@app.put("/posts/{id}")
def update_post(id: int, post: Post, db: Session = Depends(get_db)):
    stmt = select(models.Post).where(models.Post.id == id)
    post_query = db.scalars(stmt).first()
    if not post_query:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    post_query.title = post.title
    post_query.content = post.content
    post_query.published = post.published
    db.commit()
    db.refresh(post_query)
    return {"data": post_query}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db)):
    stmt = select(models.Post).where(models.Post.id == id)
    post_to_delete = db.scalars(stmt).first()
    if not post_to_delete:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    db.delete(post_to_delete)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)