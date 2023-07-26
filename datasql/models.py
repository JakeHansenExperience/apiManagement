from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)

    items = relationship("Item", back_populates="owner")


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")



class Karen(Base):
    __tablename__ = "karens"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    date = Column(String)
    onGods = Column(Integer,default=0)
    playmaker = Column(String)
    

class Birthday(Base):
    __tablename__ = "birthdays"

    id = Column(Integer, primary_key=True, index=True)
    bay = Column(String)
    name = Column(String)
    age = Column(String) 
    time = Column(String)
    

class Runner(Base):
    __tablename__ = "runners"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    status = Column(String,default="chillin")
    numFloors = Column(Integer,default=0)
    numTickets = Column(Integer,default=0)
    totalTime = Column(String, default='0')




class ExpoRunner(Base):
    __tablename__ = "expoRunners"

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String)
    status = Column(String,default="chillin")
    numFloors = Column(Integer,default=0)
    numTickets = Column(Integer,default=0)
    totalTime = Column(Integer,default=0)
    startTime = Column(String,default="")
    chillinQueue = Column(Integer)
    bayName = Column(String,default="")
    runStart = Column(Integer)
    onbreak = Column(Boolean,default=False)
    shift = Column(String)




class Leaderboard(Base):
    __tablename__ = "leaderboard"

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String)
    shift = Column(String)
    category = Column(String)
    color = Column(String)
    value = Column(Integer)
