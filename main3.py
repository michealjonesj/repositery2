from fastapi import FastAPI

app = FastAPI()

@app.get("/books/default")
async def hello(default):
    return ["Python Programming Language"]

@app.get("/books/{book_name}/{book_id}")
async def books(book_name: str, book_id: int):
    return {"Books: bookname:" + book_name + "book_id:" + book_id }
