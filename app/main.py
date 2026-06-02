import os
import time
import psycopg
from psycopg.rows import dict_row
from dotenv import load_dotenv
from fastapi import FastAPI, status, HTTPException, Response
from pydantic import BaseModel

load_dotenv()

db_password = os.getenv("DB_PASSWORD")
db_user = os.getenv("DB_USER")
db_name = os.getenv("DB_NAME")

while True:
    try:
        conn = psycopg.connect(
            host='localhost',
            dbname=db_name,
            user=db_user,
            password=db_password
        )
        cur = conn.cursor(row_factory=dict_row)
        print("Database connection was sucessull!")
        break
    except Exception as e:
        print(f"Error while connecting: {e}")
        time.sleep(2)

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True

@app.get("/")
async def root():
    return {"message": "welcome to my api!!!"}

@app.get("/posts")
def get_posts():
    cur.execute("SELECT * FROM posts")
    posts = cur.fetchall()
    return {"data": posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    cur.execute(
        "INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *",
        (post.title, post.content, post.published))
    new_post = cur.fetchone()
    conn.commit()
    return {"data": new_post}

@app.get("/posts/{id}")
def get_post(id: int):
    cur.execute("SELECT * from posts WHERE id = %s", [str(id)])
    post = cur.fetchone()
    if not post:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
    return {"post_detail": post}

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    cur.execute(
        "UPDATE posts SET title=%s, content=%s, published=%s WHERE id=%s RETURNING *",
        (post.title, post.content, post.published, str(id)))
    updated_post = cur.fetchone()
    if updated_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    conn.commit()
    return {"data": updated_post}

@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    cur.execute("DELETE FROM posts WHERE id = %s RETURNING *", [str(id)])
    deleted_post = cur.fetchone()
    conn.commit()
    if deleted_post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} does not exist")
    return Response(status_code=status.HTTP_204_NO_CONTENT)