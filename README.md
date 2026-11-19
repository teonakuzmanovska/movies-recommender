# Movie Recommendation Docker Services

This is a composition of microservices for movie recommendation. It consists of 3 services:
- movies service (CRUD operations for movies)
- reviews service (CRUD operations for movie review)
- recommendation service (logic for creating movies recommendations based on movie reviews)

## Getting Started

These instructions will help you set up and run the Movie Recommendation Service using Docker.

### Prerequisites

- Docker installed on your system

### Installation

1. Open terminal
3. Navigate to your desired location
2. Clone this repository:

   `git clone https://github.com/yourusername/movie-recommendation-service.git`

### Running

1. Open docker desktop
2. Navigate to the project directory in terminal
3. Run `docker compose up`

### Accessing The Endpoints
- `http://localhost:8000/movies` : Movies service
- `http://localhost:8000/reviews` : Reviews service
- `http://localhost:8000/recommendations` : Recommendations service
- `http://localhost:8000/movies/docs` : Movies Swagger UI
- `http://localhost:8000/reviews/docs` : Reviews Swagger UI
- `http://localhost:8000/recommendations/docs` : Recommendations Swagger UI

Kong is the only public API entry point. The application containers all listen
on port `8000` inside Docker, but they are not published directly to the host.
Kong's admin API remains private inside the Docker network and is not published
to the host.



