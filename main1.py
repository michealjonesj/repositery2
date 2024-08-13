from fastapi import FastAPI

app = FastAPI()

@app.post("/items/")
def read_items(skip : int = 0, limit : int = 10):
    return {"skip": skip, "limit": limit}