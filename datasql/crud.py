from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas


# def get_user(db: Session, user_id: int):
#     return db.query(models.User).filter(models.User.id == user_id).first()


# def get_user_by_email(db: Session, email: str):
#     return db.query(models.User).filter(models.User.email == email).first()


# def get_users(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.User).offset(skip).limit(limit).all()


# def create_user(db: Session, user: schemas.UserCreate):
#     fake_hashed_password = user.password + "notreallyhashed"
#     db_user = models.User(email=user.email, hashed_password=fake_hashed_password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user

def create_runner(db: Session, runner: schemas.RunnerCreate):
    db_runner = models.Runner(name=runner.name)
    print("HIHIHI")
    db.add(db_runner)
    db.commit()
    db.refresh(db_runner)
    return db_runner

# class ExpoRunnerCreate(BaseModel):
#     name: str
#     chillinQueue: int
#     runStart: str
#     shift: str

def create_expoRunner(db: Session, expoRunner: schemas.ExpoRunnerCreate):
    db_expoRunner = models.ExpoRunner(name=expoRunner.name,chillinQueue=expoRunner.chillinQueue,runStart=expoRunner.runStart,shift=expoRunner.shift)
    db.add(db_expoRunner)
    db.commit()
    db.refresh(db_expoRunner)
    return db_expoRunner

def get_runners(db: Session):
    return db.query(models.Runner).all()

def get_expoRunners(db: Session):
    return db.query(models.ExpoRunner).filter(models.ExpoRunner.status != "Done").all()

def get_runner_by_id(db: Session, id: int):
    return db.query(models.Runner).filter(models.Runner.id == id).first()
    


def update_runner_status(db: Session, input: schemas.UpdateRunnerStatus):
    # input.status, input.id
    db_runner = get_runner_by_id(db,input.id)
    db_runner.status = input.status
    db.commit()
    db.refresh(db_runner)
    return db_runner






def create_birthday(db: Session, birthday: schemas.BirthdayCreate):
    db_birthday = models.Birthday(
        bay=birthday.bay, name=birthday.name,age=birthday.age,time=birthday.time
    )
    db.add(db_birthday)
    db.commit()
    db.refresh(db_birthday)
    return db_birthday

def get_birthdays(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Birthday).all()

def get_birthday_by_id(db: Session, id: int):
    return db.query(models.Birthday).filter(models.Birthday.id == id).first()

def delete_birthday_by_id(db: Session, id: int):
    # done_birthday = db.get(models.Birthday, id)
    # if not done_birthday:
    #     raise HTTPException(status_code=404, detail="Birthday not found")
    try:
        done_birthday = db.query(models.Birthday).filter(models.Birthday.id == id).first()
        db.delete(done_birthday)
        db.commit()
    except:
        raise HTTPException(status_code=404, detail="Birthday not there")
    
def delete_leaderID(db:Session, id:int ):
    try:
        deleteLeader = db.query(models.Leaderboard).filter(models.Leaderboard.id == id).first()
        db.delete(deleteLeader)
        db.commit()
    except:
        raise HTTPException(status_code=404, detail="Birthday not there")

def create_karen(db: Session, karen: schemas.KarenCreate):
    db_karen = models.Karen(title=karen.title, description=karen.description,date=karen.date, playmaker=karen.playmaker)
    db.add(db_karen)
    db.commit()
    db.refresh(db_karen)
    return db_karen

def get_karen_by_id(db: Session, id: int):
    return db.query(models.Karen).filter(models.Karen.id == id).first()



def delete_all_karens(db: Session):
    num_rows_deleted = db.query(models.Karen).delete()
    db.commit()

def delete_expoRunners(db: Session):
    num_rows_deleted = db.query(models.ExpoRunner).delete()
    db.commit()

    
def get_karens(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Karen).all()

def getLeaderboard(db: Session):
    return db.query(models.Leaderboard).all()


def update_karen_onGods(db: Session, id: int):
    db_karen = get_karen_by_id(db, id)
    db_karen.onGods += 1
    db.commit()
    db.refresh(db_karen)
    return db_karen


def get_expo_runner_NameShift(db: Session, name: str, shift: str):
    db_runner = db.query(models.ExpoRunner).filter(models.ExpoRunner.name == name, models.ExpoRunner.shift == shift).first()
    
    return db_runner

def update_sidework(db: Session, input: schemas.updateStatus):
    # name shift
    db_runner = get_expo_runner_NameShift(db,input.name,input.shift)
    db_runner.status = "sidework"
    db.commit()
    db.refresh(db_runner)
    return db_runner

def doneSidework(db: Session, input: schemas.updateStatus):
    db_runner = get_expo_runner_NameShift(db,input.name,input.shift)
    db_runner.status = "chillin"
    db.commit()
    db.refresh(db_runner)
    return db_runner

def runnerUp(db: Session, input: schemas.updateRunnerUp):
    print("hihslal")
    runners = get_expoRunners(db)
    for runner in runners:
        runner.chillinQueue -= 1
    db.commit()

    db_runner = get_expo_runner_NameShift(db,input.name,input.shift)
    db_runner.status = "running"
    db_runner.numFloors += input.floors
    db_runner.runStart = input.runStart
    db.commit()
    db.refresh(db_runner)
    return db_runner



#   name: str
#     shift: str
#     chillinQueue: int
#     totalTime: int
#     numTickets: int
def runnerBack(db: Session, input: schemas.runnerBack):
    db_runner = get_expo_runner_NameShift(db,input.name,input.shift)
    db_runner.status = "chillin"
    db_runner.chillinQueue = input.chillinQueue
    db_runner.totalTime = input.totalTime
    db_runner.numTickets = input.numTickets
    db.commit()
    db.refresh(db_runner)
    return db_runner




def createLeader(db: Session, input: schemas.LeaderInput):
    db_Leader = models.Leaderboard(name=input.name,
    shift= input.shift,
    category= input.category,
    color= input.color,   
    value= input.value)
    db.add(db_Leader)
    db.commit()
    db.refresh(db_Leader)
    return db_Leader

def createLeaderboard(db: Session):
    
    leaderBoard = [
  {
    "id": 1,
    "name": "Jake",
    "shift": "string",
    "category": "Trays",
    "color": "gold",
    "value": 100
  },
  {
    "id": 2,
    "name": "Jake",
    "shift": "string",
    "category": "Trays",
    "color": "silver",
    "value": 90
  },
  {
    "id": 3,
    "name": "Jake",
    "shift": "string",
    "category": "Trays",
    "color": "bronze",
    "value": 80
  },
  {
    "id": 4,
    "name": "Jake",
    "shift": "string",
    "category": "Stairs",
    "color": "bronze",
    "value": 80
  },
  {
    "id": 5,
    "name": "Jake",
    "shift": "string",
    "category": "Stairs",
    "color": "silver",
    "value": 90
  },
  {
    "id": 7,
    "name": "Jake",
    "shift": "string",
    "category": "Stairs",
    "color": "gold",
    "value": 100
  },
  {
    "id": 8,
    "name": "rtt",
    "shift": "6-26-2023-am",
    "category": "Averages",
    "color": "gold",
    "value": 0
  },
  {
    "id": 9,
    "name": "test",
    "shift": "6-26-2023-am",
    "category": "Averages",
    "color": "bronze",
    "value": 17
  },
  {
    "id": 10,
    "name": "y",
    "shift": "6-26-2023-am",
    "category": "Averages",
    "color": "silver",
    "value": 0
  }
]

#      {
#     "id": 1,
#     "name": "Jake",
#     "shift": "string",
#     "category": "Trays",
#     "color": "gold",
#     "value": 100
#   },
    for leader in leaderBoard:
        print(leader)
        if (leader["category"] == "Averages"):
            val = 100
        else:
            val = 1
        # input={
        # name: leader["name"],
        # "shift": "string",
        # "category": leader["category"],
        # "color": leader["color"],
        # "value": val

        # }
        input = schemas.LeaderInput(
                name="Jake",
    shift= "string",
    category= "Trays",
    color= "gold",
    value= 100
        )
        createLeader(db,input)

def getLeader(db: Session, category: str,color: str):
    leader = db.query(models.Leaderboard).filter(models.Leaderboard.category == category, models.Leaderboard.color == color).first()
    
    return leader


def update_priority(db: Session, input: schemas.updatePriority):
    runners = get_expoRunners(db)
    print("thsislsls")
    for runner in runners:
        print(runner.chillinQueue)
        if(runner.status == "chillin" and runner.chillinQueue < input.curSpot):
            print("HIHIHIHIHIHIHIHIHIHIHIHI")
            runner.chillinQueue += 1
            # db.commit()
            # db.refresh(runner)
        if(runner.name == input.name):
            runner.chillinQueue = 1
    db.commit()
    # db.refresh(runners)
    return "Updated!"





def runnerDone(db: Session, input: schemas.runnerDone):
    db_runner = get_expo_runner_NameShift(db,input.name,input.shift)
    db_runner.status = "Done"
    db.commit()
    db.refresh(db_runner)

    # update Queue
    runners = get_expoRunners(db)
    for runner in runners:
        if(runner.status == "chillin" and runner.chillinQueue > input.currentQueue):
            runner.chillinQueue -= 1
            db.commit()
            db.refresh()




    leaders = getLeaderboard(db)

    tGold = 0 
    tSilver = 0
    tBronze=0
    sGold=0
    sSilver=0
    sBronze=0
    aGold=0
    aSilver=0
    aBronze =0
    for leader in leaders:
        if(leader.category == "Trays" and leader.color == "gold"):
            tGold = leader.value
        elif(leader.category == "Trays" and leader.color == "silver"):
            tSilver = leader.value
        elif(leader.category == "Trays" and leader.color == "bronze"):
            tBronze = leader.value
        elif(leader.category == "Stairs" and leader.color == "gold"):
            sGold = leader.value 
        elif(leader.category == "Stairs" and leader.color == "silver"):
            sSilver = leader.value 
        elif(leader.category == "Stairs" and leader.color == "bronze"):
            sBronze = leader.value 
        elif(leader.category == "Averages" and leader.color == "gold"):
            aGold = leader.value 
        elif(leader.category == "Averages" and leader.color == "silver"):
            aSilver = leader.value 
        elif(leader.category == "Averages" and leader.color == "bronze"):
            aBronze = leader.value 

    # trays Check
    if(input.finalTickets > tGold):
        curBronze = getLeader(db,"Trays",'bronze')
        curSilver = getLeader(db, "Trays","silver")
        curGold = getLeader(db,"Trays",'gold')
        curBronze.value = input.finalTickets
        curBronze.name = input.name
        curBronze.shift = input.shift
        curBronze.color = "gold"
        curSilver.color = "bronze"
        curGold.color = "silver"
        db.commit()
        # db.refresh()
        
    elif(input.finalTickets > tSilver):
        curBronze = getLeader(db,"Trays",'bronze')
        curSilver = getLeader(db, "Trays","silver")
        curBronze.value = input.finalTickets
        curBronze.name = input.name
        curBronze.shift = input.shift
        curBronze.color = "silver"
        curSilver.color = "bronze"
        db.commit()
        # db.refresh()

    elif(input.finalTickets > tBronze):
        curBronze = getLeader(db,"Trays","bronze")
        curBronze.value = input.finalTickets
        curBronze.name = input.name
        curBronze.shift = input.shift
        db.commit()
        # db.refresh(curBronze)

    # Stairs Check
    if(input.finalStairs > sGold):
        curBronze = getLeader(db,"Stairs",'bronze')
        curSilver = getLeader(db, "Stairs","silver")
        curGold = getLeader(db,"Stairs",'gold')
        curBronze.value = input.finalStairs
        curBronze.name = input.name
        curBronze.shift = input.shift
        curBronze.color = "gold"
        curSilver.color = "bronze"
        curGold.color = "silver"
        db.commit()
        # db.refresh()
        
    elif(input.finalStairs > sSilver):
        curBronze = getLeader(db,"Stairs",'bronze')
        curSilver = getLeader(db, "Stairs","silver")
        curBronze.value = input.finalStairs
        curBronze.name = input.name
        curBronze.shift = input.shift
        curBronze.color = "silver"
        curSilver.color = "bronze"
        db.commit()
        # db.refresh()

    elif(input.finalStairs > sBronze):
        curBronze = getLeader(db,"Stairs","bronze")
        curBronze.value = input.finalStairs
        curBronze.name = input.name
        curBronze.shift = input.shift
        db.commit()
        # db.refresh(curBronze)

# AveragesCheck
    if(input.finalAvg < aGold):
        curBronze = getLeader(db,"Averages",'bronze')
        curSilver = getLeader(db, "Averages","silver")
        curGold = getLeader(db,"Averages",'gold')
        curBronze.value = input.finalAvg
        curBronze.name = input.name
        curBronze.shift = input.shift
        curBronze.color = "gold"
        curSilver.color = "bronze"
        curGold.color = "silver"
        db.commit()
        # db.refresh()
        
    elif(input.finalAvg < aSilver):
        curBronze = getLeader(db,"Averages",'bronze')
        curSilver = getLeader(db, "Averages","silver")
        curBronze.value = input.finalAvg
        curBronze.name = input.name
        curBronze.shift = input.shift
        curBronze.color = "silver"
        curSilver.color = "bronze"
        db.commit()
        # db.refresh()

    elif(input.finalAvg < aBronze):
        curBronze = getLeader(db,"Averages","bronze")
        curBronze.value = input.finalAvg
        curBronze.name = input.name
        curBronze.shift = input.shift
        db.commit()
        # db.refresh(curBronze)

    
    

#     class runnerDone(BaseModel):
#     name: str
#     shift: str
#     finalTickets: int
#     finalStairs: int
#     finalAvg: int
#     currentQueue: int

# class LeaderBoard(BaseModel):
#     id: int
#     name: str
#     shift: str
#     category: str
#     color: str
#     value: int
    
    
# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item
