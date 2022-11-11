#Importing Frameworks and Libraries ---------------------

from fastapi import FastAPI, HTTPException , Request , Response , status
from fastapi.responses import HTMLResponse , JSONResponse
from starlette.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from typing import Optional , List

#Pydantic Class Model ---------------------------

class Item(BaseModel):
    user_id: str
    keywords: list
    description: str
    image: str
    lat: float
    lon: float

class ItemOut(BaseModel):
    id : int
    user_id: str
    keywords: list
    description: str
    image: str
    lat: float
    lon: float
    date_from : datetime
    date_to : datetime
    
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



itemStore = {}
count = 0


@app.get("/",response_class=HTMLResponse,status_code=200)
async def Default():
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
async def make_item(item: Item, response: Response):
    date = datetime.now()

    max_value = max(itemStore, key=itemStore.get, default=-1)
    max_value = max_value + 1
    itemInput = item.dict()
    itemID = {"id": max_value }
    itemDate = {"date_from": date, "date_to": date}
    resultantItem = {**itemID, **itemInput , **itemDate}
    itemStore[max_value] = resultantItem

    response.status_code = status.HTTP_201_CREATED

    return itemStore


    



@app.get("/item/{itemId}")
async def read_item(itemId: int):
    try:
        return items[id:itemId]
    except:
        raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/item/{itemId}")
async def item_Delete(itemId: int):
    try:
        return items[id:itemId]
    except:
        raise HTTPException(status_code=404, detail="Item not found")

@app.get("/items/")
async def return_items():
    print(itemStore)
    return list(itemStore.values())

    