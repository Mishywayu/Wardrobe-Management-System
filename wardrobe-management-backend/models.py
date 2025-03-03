from sqlalchemy import Column, Integer, String
from database import Base

# creating user model
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False) #Hashed password storage

    # relationship
    # clothing_items = relationship("ClothingItem", back_populates="owner", cascade="all, delete-orphan")
