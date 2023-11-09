from sqlalchemy import Column, String, Integer
from database import Base

class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), index=True)
    age = Column(String(50), index=True)