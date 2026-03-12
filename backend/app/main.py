from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.router import auth, tuits, users, interactions

app = FastAPI(
    title="Tuiter API",
    description="A simple Twitter clone API",
    version="0.1.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(auth.router)
app.include_router(tuits.router)
app.include_router(users.router)
app.include_router(interactions.router)

@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok", "message": "Tuiter API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
