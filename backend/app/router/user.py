from fastapi import APIRouter, Depends
from app.schemas.user import User
from uuid import UUID
from http import HTTPStatus
from typing import List

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.get("/{user_id}", response_model=User)
async def get_user(user_id: UUID) -> User:
    pass

@router.get("/followers/{user_id}", response_model=List[User])
async def get_followers(user_id: UUID) -> List[User]:
    pass

@router.get("/following/{user_id}", response_model=List[User])
async def get_following(user_id: UUID) -> List[User]:
    pass
