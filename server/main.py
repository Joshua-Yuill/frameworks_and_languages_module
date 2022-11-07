#Importing Frameworks and Libraries ---------------------

from fastapi import FastAPI, HTTPException , Request
from fastapi.responses import HTMLResponse , JSONResponse
#from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import random
import json

#Pydantic Class Model ---------------------------

class Item(BaseModel):
    user_id: str
    keywords: list
    description: str
    image: str
    lat: float
    lon: float
    
#------------------------------------------------

app = FastAPI() #defining "app" as fastAPI

#Cors Headers -----------------------------------
app.add_middleware(
CORSMiddleware,
allow_origins=["*"], # Allows all origins
allow_credentials=True,
allow_methods=["*"], # Allows all methods
allow_headers=["*"], # Allows all headers
)






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

items = {}

@app.post("/item/")
async def make_item(item: Item):    
    ItemID_Value = random.randint(1,100000)
    item_dict = item.dict()
    items[ItemID_Value] = item_dict # add items to dictionary
    print(items)
    return item_dict


@app.get("/item/{itemId}")
async def read_item(itemId: int):
    if itemId not in items:
        raise HTTPException(status_code=404, detail="Item not found")
    return items[id:itemId]

@app.delete("/item/{itemId}")
async def item_Delete(itemId: int):
    return items

@app.get("/items/")
async def return_items(item: Item):
    #convert dictionary to list or json
    return items