from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from jwt import PyJWKClient

from app.settings import (
    KEYCLOAK_CLIENT_ID,
    KEYCLOAK_ISSUER,
    KEYCLOAK_JWKS_URL,
    KEYCLOAK_TOKEN_URL,
)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl=KEYCLOAK_TOKEN_URL)
jwks_client = PyJWKClient(KEYCLOAK_JWKS_URL)


def authenticate_keycloak(token: str = Depends(oauth2_scheme)) -> dict:
    try:
        signing_key = jwks_client.get_signing_key_from_jwt(token)
        claims = jwt.decode(
            token,
            signing_key.key,
            algorithms=["RS256"],
            options={"verify_aud": False},
            issuer=KEYCLOAK_ISSUER,
        )
        audiences = claims.get("aud", [])
        if isinstance(audiences, str):
            audiences = [audiences]
        if KEYCLOAK_CLIENT_ID not in audiences and claims.get("azp") != KEYCLOAK_CLIENT_ID:
            raise ValueError("Token was not issued for this client")
        return claims
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired Keycloak token",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc
