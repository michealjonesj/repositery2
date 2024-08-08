from fastapi import FastAPI

app = FastAPI()

@app.delete("/items/{item_id}")
def delete_item(item_id : int):
    return {"message": f"Item {item_id} deleted"}