from fastapi import FastAPI
from models import Base
from database import engine
from database import engine, Base

app = FastAPI()

# create database tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Welcome to the Wardrobe Management API"}