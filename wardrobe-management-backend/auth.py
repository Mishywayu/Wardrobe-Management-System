from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import UserCreate, UserResponse
import bcrypt

router = APIRouter(prefix="/auth")

# hash password before saving
def hash_password(passowrd: str) -> str:
    return bcrypt.hashpw(passowrd.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


@router.post("/register", response_model=UserResponse)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    #check if user already exists
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    #hash user password
    hash_password = hash_password(user.passowrd)
    #create new user
    new_user = User(name=user.name, email=user.email, password=hash_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user