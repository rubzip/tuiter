from pydantic import BaseModel, Field
from uuid import UUID, uuid4


class Follow(BaseModel):
    follower_id: UUID = Field(..., description="Follower user ID", examples=[uuid4()])
    following_id: UUID = Field(..., description="Following user ID", examples=[uuid4()])
    created_at: datetime = Field(default_factory=datetime.now)

class Like(BaseModel):
    user_id: UUID = Field(..., description="User ID", examples=[uuid4()])
    tweet_id: UUID = Field(..., description="Tuit ID", examples=[uuid4()])
    created_at: datetime = Field(default_factory=datetime.now)

class TweetParenthood(BaseModel):
    parent_id: UUID = Field(..., description="Original tuit ID", examples=[uuid4()])
    child_id: UUID = Field(..., description="Response tuit ID", examples=[uuid4()])
