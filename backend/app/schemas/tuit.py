from datetime import datetime
from uuid import UUID
from typing import Optional, List
from pydantic import BaseModel, Field


class TuitBase(BaseModel):
    content: str = Field(
        ..., min_length=1, max_length=144, examples=["My first tweet 🤑"]
    )


class TuitCreate(TuitBase):
    parent_id: Optional[UUID] = Field(None, description="Parent tuit ID")


class Tuit(TuitBase):
    id: UUID
    user_id: UUID
    created_at: datetime
    likes_count: int = 0
    parent_id: Optional[UUID]

    class Config:
        from_attributes = True


class TuitThread(Tuit):
    parent: Optional["Tuit"] = None
    children: List["Tuit"] = []
