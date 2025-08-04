from fastapi import FastAPI, Body


app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "Welcome to learning fast api"}

@app.get('/posts')
def get_post():
    return {
        'data': 'this is your post'
    }
    
@app.post('/createpost')
def create_post(payLoad: dict = Body(...)):
    print(payLoad)
    return {
        'message': 'successfully created post'
    }