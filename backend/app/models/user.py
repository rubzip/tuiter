from pydantic import BaseModel, Field, HttpUrl
from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4


class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=20, pattern="^[a-zA-Z0-9_]+$", examples=["ulun_musk"])
    display_name: str = Field(..., max_length=50, examples=["Ulun Musk 🤑"])
    avatar_url: Optional[HttpUrl] = Field(None)
    bio: Optional[str] = Field(None, max_length=160, examples=["I am the owner of all you can see here 🤑🤑🤑🤑"])

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True
