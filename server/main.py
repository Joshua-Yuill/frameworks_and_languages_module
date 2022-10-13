from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import json

app = FastAPI()

posts = []

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
async def item():
    return {"message": "Hello World"}

@app.get("/item/{itemId}")
async def item_itemId():
    return {"message": "Hello World"}

@app.delete("/item/{itemId}")
async def item_Delete():
    return {"message": "Hello World"}

@app.get("/items/")
async def items():
    return {posts}