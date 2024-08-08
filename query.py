from fastapi import FastAPI

app = FastAPI()

@app.get('/game/{game_id}')
async def open_game(game_id : int, user_name : str | None = None):
    return {'Game ID' : game_id, 'User Name' : user_name}    