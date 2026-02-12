from app.models.model_user import User
from app.security.hashing import hash_password

def get_by_username(db, username):
    return db.query(User).filter(User.username == username)


def create_user(db, user):
    db_user = User(username=user.username, hashed_password=hash_password(user.password), role=user.role)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user