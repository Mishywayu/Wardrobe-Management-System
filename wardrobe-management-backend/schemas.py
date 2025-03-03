from pydantic import BaseModel

class UserCreate(BaseModel):  #ensures users send valid name, email and passowrd
    name: str
    email: str
    password: str

class UserResponse(BaseModel):  #controls what we return
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True