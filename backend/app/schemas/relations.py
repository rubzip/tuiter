from datetime import datetime
from uuid import UUID
from pydantic import BaseModel


class Follow(BaseModel):
    follower_id: UUID
    following_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True


class Like(BaseModel):
    user_id: UUID
    tweet_id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
