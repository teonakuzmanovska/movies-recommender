from pydantic import BaseModel, ConfigDict

class MovieBase(BaseModel):
    title: str
    description: str | None = None
    genres: str | None = None
    casts: str | None = None

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
