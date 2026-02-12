from jose import jwt, JWTError
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
from app.database import SessionLocal
from app.database import get_db
from app.core.config import settings
from app.crud import crud_user


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def create_access_token(data: dict):
    expire = datetime.now(timezone.utc) + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    data.update({"exp": expire})
    return jwt.encode(data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username = payload.get("sub")
    except JWTError:
        raise HTTPException(401, "Invalid token")

    return crud_user.get_by_username(db, username)
