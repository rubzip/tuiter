from app.model.base import TuitBase, UserBase


class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Config:
        from_attributes = True

class TuitCreate(TuitBase):
    pass

class Tuit(TuitBase):
    id: UUID = Field(default_factory=uuid4)
    user_id: UUID
    created_at: datetime = Field(default_factory=datetime.utcnow)
    likes_count: int = 0

    class Config:
          from_attributes = True
