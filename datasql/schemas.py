from typing import List, Union, Optional

from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: Union[str, None] = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True








class Karen(BaseModel):
    id: int
    title: str
    description: str
    date: str
    onGods: Optional[int] 
    playmaker: Optional[str]

    class Config:
        orm_mode = True


class KarenCreate(BaseModel):
    title: str
    description: str
    date: str
    playmaker: str

class KarenUpdate(BaseModel):
    karen_id: int



class Birthday(BaseModel):
    id: int
    bay: str
    name: str
    age: str
    time: str

    class Config:
        orm_mode = True


class BirthdayCreate(BaseModel):
    bay: str
    name: str
    age: str
    time: str

class BirthdayDelete(BaseModel):
    id: int


class UpdateRunnerStatus(BaseModel):
    id: int
    status: str

class UpdateRunnerStats(BaseModel):
    id: int
    numFloors: int
    numTickets: int

class Runner(BaseModel):
    id: int
    name: str
    status: str
    numFloors: int
    numTickets: int
    totalTime: str
    priority: int

    class Config:
        orm_mode = True


    
class RunnerCreate(BaseModel):
    name: str

# class Runner(Base):
#     __tablename__ = "runners"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     status = Column(String)
#     numFloors = Column(Integer)
#     numTickets = Column(Integer)



class ExpoRunner(BaseModel):
    id: int
    name: str
    status: str
    numFloors: int
    numTickets: int
    totalTime: int
    startTime: str
    chillinQueue: int
    bayName: str
    runStart: str
    onbreak: bool
    shift: str

    class Config:
        orm_mode = True


class ExpoRunnerCreate(BaseModel):
    name: str
    chillinQueue: int
    runStart: str
    shift: str



class updateStatus(BaseModel):
    name: str
    shift: str

class runnerBack(BaseModel):
    name: str
    shift: str
    chillinQueue: int
    totalTime: int
    numTickets: int

class runnerDone(BaseModel):
    name: str
    shift: str
    finalTickets: int
    finalStairs: int
    finalAvg: int
    currentQueue: int

class LeaderBoard(BaseModel):
    id: int
    name: str
    shift: str
    category: str
    color: str
    value: int

    class Config:
        orm_mode = True

class LeaderInput(BaseModel):
    name: str
    shift: str
    category: str
    color: str
    value: int

class updatePriority(BaseModel):
    name: str
    curSpot: int


class updateRunnerUp(BaseModel):
    name: str
    shift: str
    floors: int
    runStart: int