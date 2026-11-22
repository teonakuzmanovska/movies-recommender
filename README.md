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
3. Copy `.env.example` to `.env` and set local values for the PostgreSQL and Keycloak passwords
4. Run `docker compose up`

### Keycloak reviewer setup

Keycloak stores user accounts and authentication data. The application stores
the authenticated user's Keycloak ID as `reviewer_id` on each review.

The realm configuration in `keycloak/configs/realm-export.json` does not seed a
demo user or password. After starting the services, create a reviewer manually:

1. Open `http://localhost:8080/admin`.
2. Sign in with the Keycloak admin credentials from your local `.env` file.
3. Select the `movies-reviews` realm.
4. Go to **Users**, choose **Add user**, and create a reviewer.
5. Set a non-temporary password under **Credentials**.

Use that reviewer account to obtain a token when testing the protected review
creation, update, and delete endpoints.

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



