from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn

app = FastAPI() #instance


# nameof the function doesn't matter what matter is the instance
# @path_operation_decorator.operation_on_the_path('path')
# @app.get('/')
# def index(): # path operation function
#     return {'data':{'name': 'Rishav'}}

# @app.get('/about')
# def about():
#     return {'data': {'About page'}}

# uvicorn filename:instance --reload

@app.get('/')
def index():
    return {'data' : 'blog list'}

# here parameter is changing thr real query and we can access it through 'blog?limit=10'
@app.get('/blog')
def index(limit, published: bool):
    if published:
        return {'data' : f'{limit} published blogs from the DB'}
    else:
        return {'data' : f'{limit} blogs from the DB'}
        

# @app.get('/blog/{id}' ) 
# def show(id): # its get the id as string
#     # fetch blog with id = id
#     return {'data': id}

@app.get('/blog/unpublished' ) 
def show(id): # its get the id as string
    # fetch blog with id = id
    return {'data': 'all upublished blogs'}

# its called dynamic routing
@app.get('/blog/{id}' ) 
def show(id:int): # for get te integer value we specify 
    # fetch blog with id = id
    return {'data': id}

# this is called a model named Blog model
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

# inside the bracket we define the path
@app.post('/blog')
def create_blog(blog: Blog): # we use the blog model here and we get the value from the user to the API
    return {'data' : f"Blog is created with title as {blog.title}"}

# if __name__ == "__main__":
#     uvicorn.run(app,host="127.0.0.1", port=9000)