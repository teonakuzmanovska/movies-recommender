import os

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT", 5432)
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")
KEYCLOAK_REALM = os.environ.get("KEYCLOAK_REALM", "movies-reviews")
KEYCLOAK_CLIENT_ID = os.environ.get("KEYCLOAK_CLIENT_ID", "movies-reviews-client")
KEYCLOAK_PUBLIC_URL = os.environ.get("KEYCLOAK_PUBLIC_URL", "http://localhost:8080").rstrip("/")
KEYCLOAK_INTERNAL_URL = os.environ.get("KEYCLOAK_INTERNAL_URL", "http://keycloak:8080").rstrip("/")
KEYCLOAK_ISSUER = f"{KEYCLOAK_PUBLIC_URL}/realms/{KEYCLOAK_REALM}"
KEYCLOAK_JWKS_URL = f"{KEYCLOAK_INTERNAL_URL}/realms/{KEYCLOAK_REALM}/protocol/openid-connect/certs"
KEYCLOAK_TOKEN_URL = f"{KEYCLOAK_ISSUER}/protocol/openid-connect/token"
