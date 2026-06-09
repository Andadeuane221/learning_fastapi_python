import os
from dotenv import load_dotenv
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user

models.Base.metadata.create_all(engine)

load_dotenv()

db_password = os.getenv("DB_PASSWORD")
db_user = os.getenv("DB_USER")
db_name = os.getenv("DB_NAME")


app = FastAPI()

app.include_router(post.router)
app.include_router(user.router)

@app.get("/")
async def root():
    return {"message": "welcome to my api!!!"}
