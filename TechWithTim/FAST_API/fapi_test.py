from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    length: float
    useful: Optional[str] = None


app = FastAPI()


inventory = {
    1: {'name': 'pen',
        'length': 15.2,
        'useful': 'high'},
    2: {'name': 'rubber',
        'length': 10.5,
        'useful': 'very high'},
    3: {'name': 'tiepin',
        'length': 5.8,
        'useful': 'average'},
}


@app.get('/')
def home():
    return {'data': 'test'}


@app.get('/sr')
def second_response():
    return {'data': 'second_test'}


@app.get('/get-item/{item_id}')
def get_item(item_id: int = Path(None, description='ID of the item.', gt=0, lt=max(inventory.keys())+1)):
    return inventory[item_id]


@app.get('/get-item/{item_id}/{detail}')
def get_item_detail(item_id: int, detail: str):
    response = ''

    try:
        if inventory.get(item_id).get(detail):
            response = str(inventory[item_id][detail])
        elif inventory.get(item_id):
            response = f"No such parameter in inventory position number: {item_id}"
    except AttributeError:
        response = "No such position in inventory"

    return response


@app.get('/get-by-name')
def get_item_by_name(name: Optional[str] = None):
    for item_id in inventory:
        if inventory[item_id]['name'] == name:
            return inventory[item_id]
    return {'data': 'not found'}

    # parameter 'name' is setting by default as query parameter is not mentioned in address route
    # (name: Optional[str] = None) makes parameter optional
    # example: http://127.0.0.1:8000/get-by-name?name=rubber
    # another parameter in request can be added after &, e.g. /get-by-name?name=rubber&test=test

    # aand... mixing:


@app.get('/get-by-mixing/{item_id}')
def get_item_with_mixing(*, item_id: int, name: Optional[str] = None, test: bool):
    if inventory[item_id]['name'] == name and test:
        return inventory[item_id]['name']
    return {'data': 'not found'}


@app.post('/create-item/{item_id}')
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        return {'Error': 'Item id already exists.'}

    # inventory[item_id] = {
    #     'name': item.name,
    #     'length': item.length,
    #     'useful': item.useful
    # }
    # FastAPI can auto-replace json into class values

    inventory[item_id] = item

    return inventory[item_id]
