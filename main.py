from fastapi import FastAPI

Myapp = FastAPI() #instance


# nameof the function doesn't matter what matter is the instance
# @path_operation_decorator.operation_on_the_path('path')
@Myapp.get('/')
def index(): # path operation function
    return {'data':{'name': 'Rishav'}}

@Myapp.get('/about')
def about():
    return {'data': {'About page'}}

# uvicorn filename:instance --reload