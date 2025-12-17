from fastapi import APIRouter 

auth_hello = APIRouter(prefix='/hello', tags=['test'])
@auth_hello.get('/')
def hello():
    return 'hello'
