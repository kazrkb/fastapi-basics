# pip install "fastapi[standard]" "uvicorn[standard]" sqlalchemy python-dotenv pydantic

from typing import Optional
from fastapi import FastAPI, Body
from pydantic import BaseModel


app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    publish: bool = True
    rating: Optional[int] = None

@app.get("/")
def read_root():
    return {"Hello": "Welcome to learning fast api"}

@app.get('/posts')
def get_post():
    return {
        'data': 'this is your post'
    }
    
@app.post('/createpost')
# def create_post(payLoad: dict = Body(...)):
def create_post(new_post: Post):
    # print(payLoad)
    print(new_post)
    print(new_post.dict())
    
    return {
        # 'message': 'successfully created post',
        # 'newpost': f"title {payLoad['title']} content {payLoad['content']}"
        "data": new_post
    }