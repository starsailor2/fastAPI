from fastapi import FastAPI

myapp = FastAPI() #instance


# nameof the function doesn't matter what matter is the instance
# @path_operation_decorator.operation_on_the_path('path')
# @myapp.get('/')
# def index(): # path operation function
#     return {'data':{'name': 'Rishav'}}

# @myapp.get('/about')
# def about():
#     return {'data': {'About page'}}

# uvicorn filename:instance --reload

@myapp.get('/')
def index():
    return {'data' : 'blog list'}

# @myapp.get('/blog/{id}' ) 
# def show(id): # its get the id as string
#     # fetch blog with id = id
#     return {'data': id}

@myapp.get('/blog/unpublished' ) 
def show(id): # its get the id as string
    # fetch blog with id = id
    return {'data': 'all upublished blogs'}

# its called dynamic routing
@myapp.get('/blog/{id}' ) 
def show(id:int): # for get te integer value we specify 
    # fetch blog with id = id
    return {'data': id}

# fast api read the files line by line
 # for make them run in a proper way, the static routing is always write above the dynamic routing.