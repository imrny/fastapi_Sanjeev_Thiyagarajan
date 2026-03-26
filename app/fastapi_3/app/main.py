from passlib.context import CryptContext
from typing import Optional, List
from fastapi import FastAPI, Response, status, HTTPException, Depends
from fastapi import Body
from pydantic import BaseModel
from random import randrange
import psycopg
from psycopg.rows import dict_row
import time
from datetime import datetime
from sqlalchemy.orm import Session
from . import models, schemas, utils
from .models import  Post
from .database import engine, get_db
from .routers import post, user, auth


#pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


#class Post(BaseModel):
#    title: str
#    content: str
#    published: bool = True

while True:
    try:
        conn = psycopg.connect(host='192.168.1.101', dbname='fastapi', user='postgres', password='3un13una', row_factory=dict_row)
        cursor = conn.cursor()
        print("database connection was successful")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("error: ", error)
        time.sleep(10)

#my_posts = [{"title": "post1", "content": "hello", "id": 1}, {"title": "post2", "content": "world", "id": 2}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p
        
def find_index_post(id):
    #for i, p in enumerate(my_posts):
    for i, p in reversed(list(enumerate(my_posts))):
        if p["id"] == id:
            return i
                
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
async def root():
    return {"Hello World"}

