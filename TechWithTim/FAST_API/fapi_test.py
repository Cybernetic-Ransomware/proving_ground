from fastapi import FastAPI

app = FastAPI()

inventory = {
    1: {'name': 'pen',
        'length': 'short',
        'useful': 'high'},
    2: {'name': 'rubber',
        'length': 'mid',
        'useful': 'very high'},
    3: {'name': 'tiepin',
        'length': 'mid',
        'useful': 'average'},
}


@app.get('/')
def home():
    return {'data': 'test'}


@app.get('/sr')
def second_response():
    return {'data': 'second_test'}


@app.get('/get-item/{item_id}')
def get_item(item_id: int):
    return inventory[item_id]
