from datetime import datetime
import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey, UniqueConstraint, Integer
from app.database import Base


class FollowDB(Base):
    __tablename__ = "follows"   
    __table_args__ = (
        UniqueConstraint("follower_id", "following_id", name="unique_follow"),
    )
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    follower_id = Column(String(36), ForeignKey("users.id"), nullable=False)
    following_id = Column(String(36), ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)


class LikeDB(Base):
    __tablename__ = "likes"
    __table_args__ = (
        UniqueConstraint("user_id", "tweet_id", name="unique_like"),
    )
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False)
    tweet_id = Column(String(36), ForeignKey("tuits.id"), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
