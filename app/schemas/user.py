from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    admin: bool

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    username: str
    admin: bool


class UserDetails(BaseModel):
    id: str


class UserExists(BaseModel):
    user_exists: bool


class Message(BaseModel):
    msg: str
