from typing import Union
from fastapi import FastAPI

app = FastAPI()
@app.get('/')
def read_root():
    return {'Hello world!!!'}

@app.get('/hello')
def hello_world():
    return {'Hello world!!! form GET /hello'}