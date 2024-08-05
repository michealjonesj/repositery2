from fastapi import FastAPI
app = FastAPI()
@app.get("/difference")
def Diff(num1: int, num2 : int):
    return {"Difference" : num1 - num2 }