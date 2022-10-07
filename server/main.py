from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return ("Hello world")

@app.get("/item/")
async def root():
    return ("Hello world")