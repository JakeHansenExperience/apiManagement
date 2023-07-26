from typing import List

from fastapi import Depends, FastAPI, HTTPException, WebSocket
from fastapi.security import OAuth2PasswordBearer
from typing_extensions import Annotated
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")





# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





# @app.post("/users/", response_model=schemas.User)
# def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
#     db_user = crud.get_user_by_email(db, email=user.email)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return crud.create_user(db=db, user=user)


# @app.get("/users/", response_model=List[schemas.User])
# def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     users = crud.get_users(db, skip=skip, limit=limit)
#     return users


# @app.get("/users/{user_id}", response_model=schemas.User)
# def read_user(user_id: int, db: Session = Depends(get_db)):
#     db_user = crud.get_user(db, user_id=user_id)
#     if db_user is None:
#         raise HTTPException(status_code=404, detail="User not found")
#     return db_user



@app.post("/runner", response_model=schemas.Runner,tags=["Runners"])
def create_runner(input: schemas.RunnerCreate,db: Session = Depends(get_db)):
    print("Hi")
    return crud.create_runner(db=db,runner=input)

@app.get("/runners", response_model=List[schemas.Runner], tags=["Runners"])
def get_runners(db: Session = Depends(get_db)):
    runners = crud.get_runners(db)
    return runners

@app.put("/updateRunnerStatus",tags=["Runners"] )
def update_runner_status(input: schemas.UpdateRunnerStatus, db: Session = Depends(get_db)):
    crud.update_runner_status(db=db, input=input)

# @app.up("/updateRunnerStats", tags=[])

@app.post("/birthday", response_model=schemas.Birthday,tags=["Birthday"])
def create_birthday(input: schemas.BirthdayCreate, db: Session = Depends(get_db)):
    return crud.create_birthday(db=db,birthday=input)

@app.get("/birthdays", response_model=List[schemas.Birthday],tags=["Birthday"])
def get_birthdays(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    birthdays = crud.get_birthdays(db,skip=skip,limit=limit)
    return birthdays

@app.delete("/deleteBirthdayByID", tags=["Birthday"])
def delete_birthday_by_id(birthday_id: int, db: Session = Depends(get_db)):
    return crud.delete_birthday_by_id(db=db, id=birthday_id)


@app.post("/karen", response_model=schemas.Karen,tags=["Karen"])
def create_karen(input: schemas.KarenCreate, db: Session = Depends(get_db)):
    return crud.create_karen(db=db,karen=input)

@app.post("/expoRunner", response_model=schemas.ExpoRunner,tags=["ExpoRunner"])
def create_expoRunner(input:schemas.ExpoRunnerCreate, db: Session = Depends(get_db)):
    print(input)
    return crud.create_expoRunner(db=db,expoRunner=input)

@app.get("/expoRunner", response_model= List[schemas.ExpoRunner],tags=["ExpoRunner"])
def get_expoRunners(db: Session = Depends(get_db)):
    runners = crud.get_expoRunners(db)
    return runners

@app.get("/karen", response_model=schemas.Karen,tags=["Karen"])
def get_karen_by_id(karen_id: int, db: Session = Depends(get_db)):
    return crud.get_karen_by_id(db=db, id=karen_id)




@app.delete("/karen",tags=["Karen"])
def delete_karen_by_id(karen_id: int, db: Session = Depends(get_db)):
    return crud.delete_karen_by_id(db=db, id=karen_id )



@app.delete("/karens",tags=["Karen"])
def delete_all_karens(db: Session = Depends(get_db)):
    return crud.delete_all_karens(db=db)

@app.get("/karens", response_model=List[schemas.Karen],tags=["Karen"])
def get_karens(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    karens = crud.get_karens(db,skip=skip,limit=limit)
    return karens

@app.put("/updateKarenOnGods",tags=["Karen"] )
def update_karen_onGod(input: schemas.KarenUpdate, db: Session = Depends(get_db)):
    print("Hihihi")
    crud.update_karen_onGods(db=db, id=input.karen_id)


@app.put("/updateSideworkFromExpo", tags=["ExpoRunner"])
def update_sidework_FromExpo(input: schemas.updateStatus, db: Session = Depends(get_db)):
    crud.update_sidework(db=db, input=input)

@app.delete("/deleteExpoRunners", tags=["ExpoRunner"])
def delete_expoRunners(db: Session = Depends(get_db)):
    crud.delete_expoRunners(db=db)

@app.put("/updateBackRunninFromExpo", tags=["ExpoRunner"])
def doneSidework(input: schemas.updateStatus, db: Session = Depends(get_db)):
    crud.doneSidework(db,input)

@app.put("/updateRunnerUp", tags=["ExpoRunner"])
def nowRunning(input: schemas.updateRunnerUp, db: Session = Depends(get_db)):
    print("JOsa;")
    crud.runnerUp(db,input)

@app.put("/updateRunnerBack", tags=["ExpoRunner"])
def runnerBack(input: schemas.runnerBack, db: Session = Depends(get_db)):
    crud.runnerBack(db, input)

@app.post("/createLeader", tags=["ExpoRunner"])
def createLeader(input:schemas.LeaderInput,db: Session = Depends(get_db)):
    crud.createLeader(db,input)

@app.get("/leaderboard", tags=["ExpoRunner"],response_model= List[schemas.LeaderBoard])
def getLeaderboard(db: Session = Depends(get_db)):
    leaders = crud.getLeaderboard(db)
    return leaders

@app.put("/updateRunnerDone", tags=["ExpoRunner"])
def runnerDone(input: schemas.runnerDone, db: Session = Depends(get_db)):
    print("HEREEEEEEEEEE")
    crud.runnerDone(db,input)

@app.delete("/deleteLeader",tags=["ExpoRunner"])
def delete_leaderID(id: int, db: Session = Depends(get_db)):
    return crud.delete_leaderID(db=db, id=id )

@app.put("/updatePriority", tags=["ExpoRunner"])
def updatePriority(input: schemas.updatePriority, db: Session = Depends(get_db)):
    return crud.update_priority(db=db, input=input)

@app.post("/setUpLeaderboard", tags=["ExpoRunner"])
def createLeaderboard(db: Session = Depends(get_db)):
    return crud.createLeaderboard(db)
# @app.post("/users/{user_id}/items/", response_model=schemas.Item)
# def create_item_for_user(
#     user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
# ):
#     return crud.create_user_item(db=db, item=item, user_id=user_id)


# @app.get("/items/", response_model=List[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items