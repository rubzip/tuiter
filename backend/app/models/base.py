from pydantic import BaseModel, Field, HttpUrl


class UserBase(BaseModel):
    username: str = Field(..., min_length=3, max_length=20, pattern="^[a-zA-Z0-9_]+$", examples=["ulun_musk"])
    display_name: str = Field(..., max_length=50, examples=["Ulun Musk 🤑"])
    avatar_url: Optional[HttpUrl] = Field(None)
    bio: Optional[str] = Field(None, max_length=160, examples=["I am the owner of all you can see here 🤑🤑🤑🤑"])

class TuitBase(BaseModel):
    content: str = Field(..., min_length=1, max_length=280, examples=["My first tweet 🤑"])
