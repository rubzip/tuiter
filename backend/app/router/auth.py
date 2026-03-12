from fastapi import APIRouter

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

# Placeholder for future auth endpoints
@router.post("/register")
async def register():
    pass

@router.post("/login")
async def login():
    pass
