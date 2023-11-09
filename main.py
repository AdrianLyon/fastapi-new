from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
from database import engine, localSession
from schemas import PlayerData, PlayerId
from models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()

@app.get('/api/players/', response_model=list[PlayerId])
def get_players(db: Session = Depends(get_db)):
    return crud.get_players(db=db)

@app.get('/api/players/{id:int}', response_model=PlayerId)
def get_player(db: Session = Depends(get_db)):
    player_by_id = crud.get_player_by_id(db=db, id=id)
    if player_by_id:
        return player_by_id
    raise HTTPException(status_code=404, detail='Player not Found')

@app.post('/api/players/', response_model=PlayerId)
def create_player(player: PlayerData, db: Session = Depends(get_db)):
    return crud.create_player(db=db, player=player)