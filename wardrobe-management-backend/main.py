from fastapi import FastAPI
from database import engine, Base

app = FastAPI()

# create dataase tables
Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message": "Welcome to the Wardrobe Management API"}