from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return """
    <html>
        <head>
            <title>I'm Sorry I think You're Lost....</title>
        </head>
        <body>
            <h1>I'm Sorry I think You're Lost....</h1><br>
            <h2>This is not the page you are looking for</h2>
        </body>
    </html>
    """

@app.post("/item/")
async def item():
    return {"message": "Hello World"}

@app.get("/item/{itemId}")
async def item():
    return {"message": "Hello World"}

@app.delete("/item/{itemId}")
async def item():
    return {"message": "Hello World"}

@app.get("/items/")
async def item():
    return {"message": "Hello World"}