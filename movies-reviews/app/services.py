from fastapi import HTTPException
from app.models import Review
from sqlalchemy.orm import Session
import requests

def get_reviews(db: Session, offset: int = 0, limit: int = 100):
    return db.query(Review).offset(offset).limit(limit).all()

def add_review(db: Session, review, reviewer_id: str):
    movie_url = f"http://movie_service:8000/movies-crud/movies/{review.movie_id}"
    movie_response = requests.get(movie_url, timeout=10)
    print(movie_response)
    if movie_response.status_code != 200:
        raise HTTPException(status_code=404, detail="Movie not found")
    movie = movie_response.json()
    db_review = Review(**review.model_dump(), reviewer_id=reviewer_id, movie=movie)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

def update_review_by_id(db: Session, review_id: int, review, reviewer_id: str):
    db_review = db.query(Review).filter(Review.id == review_id).first()
    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    if db_review.reviewer_id != reviewer_id:
        raise HTTPException(status_code=403, detail="You can only update your own reviews")
    db_review.comment = review.comment
    db_review.rating = review.rating
    db.commit()
    db.refresh(db_review)
    return db_review

def delete_review_by_id(db: Session, review_id: int, reviewer_id: str):
    db_review = db.query(Review).filter(Review.id == review_id).first()
    if db_review is None:
        raise HTTPException(status_code=404, detail="Review not found")
    if db_review.reviewer_id != reviewer_id:
        raise HTTPException(status_code=403, detail="You can only delete your own reviews")
    db.delete(db_review)
    db.commit()
    return db_review
