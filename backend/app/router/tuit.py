from fastapi import APIRouter, Depends
from app.schemas.tuit import Tuit, TuitCreate, TuitThread
from app.schemas.relations import Like
from uuid import UUID
from http import HTTPStatus


router = APIRouter(
    prefix="/tuits",
    tags=["Tuits"]
)

@router.post("/", response_model=Tuit, status_code=HTTPStatus.CREATED)
async def create_tuit(tuit: TuitCreate):
    """Creates a new tuit."""
    pass

@router.post("/{parent_id}/respond", response_model=Tuit)
async def respond_tuit(parent_id: UUID, tuit: TuitCreate):
    """Creates tuit as response of other."""
    pass

@router.delete("/{tuit_id}", status_code=HTTPStatus.NO_CONTENT)
async def delete_tuit(tuit_id: UUID):
    """Delete specific tuit by id"""
    pass

@router.get("/{tuit_id}", response_model=Tuit)
async def get_tuit(tuit_id: UUID):
    """Gets specific tuit."""
    pass

@router.get("/{tuit_id}/thread", response_model=TuitThread)
async def get_thread(tuit_id: UUID, limit: int = 50):
    """Gets specific tuit thread."""
    pass
