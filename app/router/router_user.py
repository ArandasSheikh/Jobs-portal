from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.schemas_user import UserCreate, UserOut
from app.crud.crud_user import create_user, get_by_username
# from app.security.token import OAuth2PasswordRequestForm
from fastapi.security import OAuth2PasswordRequestForm
from app.security.hashing import verify_password
from app.security.token import create_access_token

router = APIRouter()

@router.post('/signup', response_model=UserOut)
def signup(user: UserCreate, db: Session = Depends(get_db)):
    if get_by_username(db, user.username):
        raise HTTPException(status_code=400, detail="User already exists")
    return create_user(db, user)


@router.post('/login')
def login(form: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_by_username(db, form.username)
    if not user or not verify_password(form.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    return {"access_token": create_access_token(data={"sub": user.username}), "token_type": "bearer"}


