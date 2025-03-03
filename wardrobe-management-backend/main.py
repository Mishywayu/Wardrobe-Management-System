from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth import router as auth_router
from database import engine
import models

# Create database tables
models.Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI()

app.include_router(auth_router)

@app.get("/")
def home():
    return {"message": "Welcome to the Wardrobe Management API"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)