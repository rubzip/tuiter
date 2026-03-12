from datetime import datetime
import uuid
from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from app.database import Base


class TuitDB(Base):
    __tablename__ = "tuits"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    content = Column(String, nullable=False)
    user_id = Column(String(36), ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    parent_id = Column(String(36), ForeignKey("tuits.id"), nullable=True)
    likes_count = Column(Integer, nullable=False, default=0)
