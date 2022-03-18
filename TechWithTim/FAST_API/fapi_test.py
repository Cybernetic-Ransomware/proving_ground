from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def home():
    return {'data': 'test'}


@app.get('/sr')
def second_response():
    return {'data': 'second_test'}
