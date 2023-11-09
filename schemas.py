from pydantic import BaseModel

class PlayerData(BaseModel):
    name: str
    age: str

class PlayerId(PlayerData):
    id:int