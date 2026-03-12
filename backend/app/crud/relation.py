from typing import Optional, List
from uuid import UUID
from sqlalchemy.orm import Session
from app.models.relations import FollowDB, LikeDB
from app.crud.user import get_user
from app.crud.tuit import get_tuit


# --- Read Operations (Checkers) ---

def is_following(db: Session, follower_id: UUID, following_id: UUID) -> bool:
    """Check if a user is following another."""
    return db.query(FollowDB).filter(
        FollowDB.follower_id == str(follower_id), 
        FollowDB.following_id == str(following_id)
    ).first() is not None


def is_liking(db: Session, user_id: UUID, tuit_id: UUID) -> bool:
    """Check if a user likes a specific tuit."""
    return db.query(LikeDB).filter(
        LikeDB.user_id == str(user_id), 
        LikeDB.tweet_id == str(tuit_id)
    ).first() is not None


def get_likes_by_user(db: Session, user_id: UUID, limit: int = 10, offset: int = 0) -> List[LikeDB]:
    """Fetch all likes from a specific user."""
    return (
        db.query(LikeDB)
        .filter(LikeDB.user_id == str(user_id))
        .limit(limit)
        .offset(offset)
        .all()
    )


# --- Write Operations (Interactions) ---

def follow(db: Session, follower_id: UUID, following_id: UUID) -> Optional[FollowDB]:
    """Create a follow relationship and update follower count for the target."""
    if is_following(db, follower_id, following_id) or follower_id == following_id:
        return None
    
    db_follow = FollowDB(
        follower_id=str(follower_id), 
        following_id=str(following_id)
    )
    db.add(db_follow)
    
    # Update follower count for the user being followed
    db_user = get_user(db, following_id)
    if db_user:
        db_user.follower_count += 1
    
    db.commit()
    db.refresh(db_follow)
    return db_follow


def unfollow(db: Session, follower_id: UUID, following_id: UUID) -> Optional[FollowDB]:
    """Remove a follow relationship and update follower count for the target."""
    db_follow = db.query(FollowDB).filter(
        FollowDB.follower_id == str(follower_id), 
        FollowDB.following_id == str(following_id)
    ).first()
    
    if not db_follow:
        return None
        
    db.delete(db_follow)
    
    # Update follower count
    db_user = get_user(db, following_id)
    if db_user:
        db_user.follower_count -= 1
        
    db.commit()
    return db_follow


def like(db: Session, user_id: UUID, tuit_id: UUID) -> Optional[LikeDB]:
    """Like a tuit and update its like count."""
    if is_liking(db, user_id, tuit_id):
        return None
        
    db_like = LikeDB(user_id=str(user_id), tweet_id=str(tuit_id))
    db.add(db_like)
    
    # Update tuit likes count
    db_tuit = get_tuit(db, tuit_id)
    if db_tuit:
        db_tuit.likes_count += 1
        
    db.commit()
    db.refresh(db_like)
    return db_like


def unlike(db: Session, user_id: UUID, tuit_id: UUID) -> Optional[LikeDB]:
    """Unlike a tuit and update its like count."""
    db_like = db.query(LikeDB).filter(
        LikeDB.user_id == str(user_id), 
        LikeDB.tweet_id == str(tuit_id)
    ).first()
    
    if not db_like:
        return None
        
    db.delete(db_like)
    
    # Update tuit likes count
    db_tuit = get_tuit(db, tuit_id)
    if db_tuit:
        db_tuit.likes_count -= 1
        
    db.commit()
    return db_like
