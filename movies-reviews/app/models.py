from app.database import Base
from sqlalchemy import Column, Float, Integer, PickleType, String, Text

class Review(Base):
    __tablename__ = 'reviews'

    id = Column(Integer, primary_key=True, index=True)
    movie_id = Column(Integer, index=True)
    reviewer_id = Column(String(255), nullable=False, index=True)
    rating = Column(Float)
    comment = Column(Text)
    movie = Column(PickleType)
