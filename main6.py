from enum import Enum
from fastapi import FastAPI

app = FastAPI()

class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'

@app.get('model/{model_name}') 
async def get_model(model_name : ModelName):
    if model_name is ModelName.alexnet:
        return {"Model Name " : model_name}
    if model_name is ModelName.resnet:
        return {'Model Name ' : model_name}
    else:
        return {'Model name ' : model_name}

   