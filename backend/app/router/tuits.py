from fastapi import APIRouter, Depends
from models.base import TweetBase
from models.relations import Like


router = APIRouter(
    prefix="/tuits",
    tags=["Tuits"]
)

@router.post("/", response_model=Tuit, status_code=status.HTTP_201_CREATED)
async def create_tuit(tuit: TuitCreate):
    """Creates a new tuit."""
    pass

@router.post("/{parent_id}/respond", response_model=Tuit)
async def respond_tuit(parent_id: UUID, tuit: TuitCreate):
    """Creates tuit as response of other."""
    pass

@router.delete("/{tuit_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_tuit(tuit_id: UUID):
    """Delete specific tuit by id"""
    pass

@router.get("/{tuit_id}", response_model=Tuit)
async def get_tuit(tuit_id: UUID):
    """Gets specific tuit."""
    pass
