from typing import Optional, List
from uuid import UUID
from sqlalchemy.orm import Session
from app.models.user import UserDB
from app.models.relations import FollowDB
from app.schemas.user import UserCreate


# --- Read Operations ---

def get_user(db: Session, user_id: UUID) -> Optional[UserDB]:
    """Fetch a single user by UUID."""
    return db.query(UserDB).filter(UserDB.id == str(user_id)).first()


def get_user_by_username(db: Session, username: str) -> Optional[UserDB]:
    """Fetch a single user by username."""
    return db.query(UserDB).filter(UserDB.username == username).first()


def get_users(db: Session, limit: int = 10, offset: int = 0) -> List[UserDB]:
    """Fetch a list of users with pagination."""
    return db.query(UserDB).limit(limit).offset(offset).all()


def get_followers(db: Session, user_id: UUID, limit: int = 10, offset: int = 0) -> List[UserDB]:
    """Fetch all users following a specific user."""
    return (
        db.query(UserDB)
        .join(FollowDB, FollowDB.follower_id == UserDB.id)
        .filter(FollowDB.following_id == str(user_id))
        .limit(limit)
        .offset(offset)
        .all()
    )


def get_following(db: Session, user_id: UUID, limit: int = 10, offset: int = 0) -> List[UserDB]:
    """Fetch all users a specific user is following."""
    return (
        db.query(UserDB)
        .join(FollowDB, FollowDB.following_id == UserDB.id)
        .filter(FollowDB.follower_id == str(user_id))
        .limit(limit)
        .offset(offset)
        .all()
    )


# --- Write Operations ---

def create_user(db: Session, user_in: UserCreate, hashed_password: str) -> Optional[UserDB]:
    """Create a new user. Returns None if username already exists."""
    if get_user_by_username(db, user_in.username):
        return None
    
    db_user = UserDB(
        username=user_in.username,
        display_name=user_in.display_name,
        hashed_password=hashed_password,
        avatar_url=str(user_in.avatar_url) if user_in.avatar_url else None,
        bio=user_in.bio,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def modify_user(db: Session, user_id: UUID, user_modified: UserCreate) -> Optional[UserDB]:
    """Update user information (profile fields)."""
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    
    db_user.username = user_modified.username
    db_user.display_name = user_modified.display_name
    db_user.avatar_url = str(user_modified.avatar_url) if user_modified.avatar_url else None
    db_user.bio = user_modified.bio
    
    db.commit()
    db.refresh(db_user)
    return db_user


def modify_password(db: Session, user_id: UUID, hashed_password: str) -> Optional[UserDB]:
    """Update user password."""
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    db_user.hashed_password = hashed_password
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: UUID) -> Optional[UserDB]:
    """Delete a user."""
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    db.delete(db_user)
    db.commit()
    return db_user
