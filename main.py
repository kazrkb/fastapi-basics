# pip install "fastapi[standard]" "uvicorn[standard]" sqlalchemy python-dotenv pydantic

from typing import Optional
from fastapi import FastAPI, Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    publish: bool = True
    rating: Optional[int] = None

my_posts = [{
    "title": "title of post 1",
    "content": "content of post 1",
    "publish": True,
    "rating": 3.5,
    "id": 1
}, {
    "title": "title of post 2",
    "content": "content of post 2",
    "publish": True,
    "rating": 4,
    "id": 2
}]
@app.get("/")
def read_root():
    return {"Hello": "Welcome to learning fast api"}

@app.get('/posts')
def get_posts():
    # Ensuring we return the my_posts list
    return {"data": my_posts}

@app.post('/posts')
# def create_post(payLoad: dict = Body(...)):
def create_post(new_post: Post):
    my_posts.append(new_post.dict())
    
    return {
        # 'message': 'successfully created post',
        # 'newpost': f"title {payLoad['title']} content {payLoad['content']}"
        "data": new_post
    }
