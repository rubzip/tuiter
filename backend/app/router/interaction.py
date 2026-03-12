from fastapi import APIRouter, Depends
from app.schemas.user import User
from uuid import UUID
from http import HTTPStatus


router = APIRouter(
    prefix="/interactions",
    tags=["Interactions"]
)

@router.post("/follow/{user_id}")
async def follow(user_id: UUID):
    pass

@router.post("/unfollow/{user_id}")
async def unfollow(user_id: UUID):
    pass

@router.post("/like/{tuit_id}")
async def like(tuit_id: UUID):
    pass

@router.post("/unlike/{tuit_id}")
async def unlike(tuit_id: UUID):
    pass
