from sqlalchemy.orm import Session
from models import Player
from schemas import PlayerData

def get_players(db: Session):
    return db.query(Player).all()

def get_player_by_id(db: Session, id: int):
    return db.query(Player).filter(Player.id == id).first()

def create_player(db: Session, player: PlayerData):
    new_player = Player(name=player.name, age=player.age)
    db.add(new_player)
    db.commit()
    db.flush(new_player)
    return new_player