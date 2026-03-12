from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
from uuid import UUID, uuid4


class TuitBase(BaseModel):
    content: str = Field(..., min_length=1, max_length=280, examples=["My first tweet 🤑"])

class TuitCreate(TuitBase):
    pass

class Tuit(TuitBase):
    id: UUID = Field(default_factory=uuid4)
    user_id: UUID
    created_at: datetime = Field(default_factory=datetime.utcnow)
    likes_count: int = 0

    class Config:
          from_attributes = True

class TuitThread(Tuit):
    parent: Optional[UUID]
    children: List[UUID]
