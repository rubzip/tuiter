from typing import Optional, List
from uuid import UUID
from sqlalchemy.orm import Session
from app.models.tuit import TuitDB
from app.models.relations import FollowDB


# --- Read Operations ---

def get_tuit(db: Session, tuit_id: UUID) -> Optional[TuitDB]:
    """Fetch a single tuit by UUID."""
    return db.query(TuitDB).filter(TuitDB.id == str(tuit_id)).first()


def get_tuits(db: Session, limit: int = 10, offset: int = 0) -> List[TuitDB]:
    """Fetch a list of all tuits with pagination, ordered by most recent."""
    return db.query(TuitDB).order_by(TuitDB.created_at.desc()).limit(limit).offset(offset).all()


def get_tuits_by_user(db: Session, user_id: UUID, limit: int = 10, offset: int = 0) -> List[TuitDB]:
    """Fetch tuits from a specific user."""
    return (
        db.query(TuitDB)
        .filter(TuitDB.user_id == str(user_id))
        .order_by(TuitDB.created_at.desc())
        .limit(limit)
        .offset(offset)
        .all()
    )


def get_tuits_by_following(db: Session, user_id: UUID, limit: int = 10, offset: int = 0) -> List[TuitDB]:
    """Fetch tuits from users followed by a specific user (Feed)."""
    return (
        db.query(TuitDB)
        .join(FollowDB, FollowDB.following_id == TuitDB.user_id)
        .filter(FollowDB.follower_id == str(user_id))
        .order_by(TuitDB.created_at.desc())
        .limit(limit)
        .offset(offset)
        .all()
    )


def get_children_tuits(db: Session, tuit_id: UUID, limit: int = 10, offset: int = 0) -> List[TuitDB]:
    """Fetch all responses to a specific tuit."""
    return (
        db.query(TuitDB)
        .filter(TuitDB.parent_id == str(tuit_id))
        .order_by(TuitDB.created_at.asc())
        .limit(limit)
        .offset(offset)
        .all()
    )


def get_parent_tuit(db: Session, tuit_id: UUID) -> Optional[TuitDB]:
    """Fetch the parent tuit of a specific tuit."""
    tuit = get_tuit(db, tuit_id)
    if tuit and tuit.parent_id:
        return get_tuit(db, tuit.parent_id)
    return None


# --- Write Operations ---

def create_tuit(db: Session, user_id: UUID, content: str, parent_id: Optional[UUID] = None) -> TuitDB:
    """Create a new tuit."""
    db_tuit = TuitDB(
        user_id=str(user_id), 
        content=content, 
        parent_id=str(parent_id) if parent_id else None
    )
    db.add(db_tuit)
    db.commit()
    db.refresh(db_tuit)
    return db_tuit


def remove_tuit(db: Session, tuit_id: UUID) -> Optional[TuitDB]:
    """Delete a tuit by UUID."""
    db_tuit = get_tuit(db, tuit_id)
    if db_tuit:
        db.delete(db_tuit)
        db.commit()
    return db_tuit


def remove_tuit_protected(db: Session, tuit_id: UUID, user_id: UUID) -> Optional[TuitDB]:
    """Delete a tuit only if it belongs to the specified user."""
    db_tuit = get_tuit(db, tuit_id)
    if db_tuit and db_tuit.user_id == str(user_id):
        db.delete(db_tuit)
        db.commit()
        return db_tuit
    return None
