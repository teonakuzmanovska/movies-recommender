from pydantic import BaseModel, ConfigDict

class ReviewBase(BaseModel):
    rating: float | None = None
    comment: str | None = None

class ReviewCreate(ReviewBase):
    movie_id: int

class Review(ReviewBase):
    id: int
    movie_id: int
    reviewer_id: str
    movie: dict | None = None
    model_config = ConfigDict(from_attributes=True)
