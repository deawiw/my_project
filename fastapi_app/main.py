from fastapi import FastAPI
from fastapi_app import crud, schemas
from fastapi_app.database import database

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.post("/users/", response_model=schemas.UserCreate)
async def create_user(user: schemas.UserCreate):
    return await crud.create_user(user)

@app.get("/users/", response_model=list[schemas.UserCreate])
async def get_users():
    return await crud.get_users()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}