from enum import Enum
from fastapi import FastAPI

class GameName(str, Enum):
    freefire = 'Free Fire'
    pubg = 'PubG'
    cod = 'Call Of Duty'

app = FastAPI()

@app.get("/games/{game}")
async def get_game_name(game: GameName):
    if game is GameName.freefire:
        return {'Message' : 'Wow You Choosen the game Free Fire'}
    elif game is GameName.pubg:
        return {'Message' : 'Wow You Choosen the game PubG' }
    else:
        return {'Message' : 'Wow You Choosen the game Call Of Duty' }
