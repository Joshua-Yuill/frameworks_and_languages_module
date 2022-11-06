#Importing Frameworks and Libraries ---------------------

from fastapi import FastAPI, HTTPException , Request
from fastapi.responses import HTMLResponse
#from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#--------------------------------------------------------


app = FastAPI() #defining "app" as fastAPI


#Cors Headers -----------------------------------

app.add_middleware(
CORSMiddleware,
allow_origins=["*"], # Allows all origins
allow_credentials=True,
allow_methods=["*"], # Allows all methods
allow_headers=["*"], # Allows all headers
)

#------------------------------------------------

#Pydantic Class Model ---------------------------

class Post(BaseModel):
    user_id: str
    keywords: list
    description: str
    image: str
    lat: float
    lon: float
    
#------------------------------------------------

items = [
    {"id": 0,"user_id": "user1234", "keywords": ["hammer","nails","tools"],"description":"A hammer and nails set","image":"https://placekitten.com/200/300","lat":51.2798438,"lon":1.0830275,"date_from": "2022-10-20T14:34:02.373Z","date_to":"2022-10-20T14:34:02.373Z"},
    {"id": 1,"user_id": "user5678", "keywords": ["phone","charger","plug"],"description":"A phone with charger and plug","image":"https://placekitten.com/200/300","lat":51.2798438,"lon":1.0830275,"date_from": "2022-10-20T14:34:02.373Z","date_to":"2022-10-20T14:34:02.373Z"}
]


@app.get("/",response_class=HTMLResponse,status_code=200)
async def root():
    return """
    <html>
        <head>
            <title>I'm Sorry I think You're Lost....</title>
        </head>
        <body>
            <h1>I'm Sorry I think You're Lost....</h1>
            <h2>This is not the page you are looking for</h2>
        </body>
    </html>
    """

@app.post("/item/")
async def make_item(items: Post):
    return items

@app.get("/item/{itemId}")
async def read_item(itemId: int):
    if itemId not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[id:itemId]

@app.delete("/item/{itemId}")
async def item_Delete(itemId: int):
    if itemId not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return

@app.get("/items/")
async def return_items():
    return items