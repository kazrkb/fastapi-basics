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
    post_dict = new_post.dict()
    post_dict['id'] = randrange(1, 1000000)
    my_posts.append(post_dict)
    return {
        "data": post_dict
    }
@app.get("/posts/{id}")
def get_single_post(id):
    print(id)
    return {
        "post_data": f"This is the post with id {id}"
    }

