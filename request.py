from fastapi import FastAPI
from pydantic import BaseModel

class UserData(BaseModel):
    name : str
    id : int
    about : str = None

app = FastAPI()
@app.post('/user/')
async def create_data(user_data : UserData):
    return user_data

    