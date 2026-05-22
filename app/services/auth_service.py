from sqlalchemy.orm import Session

from app.repositories.user_repository import get_user_by_phone, create_user

from app.core.security import hash_password, verify_password, create_access_token


def register_user(
    db: Session, phone: str, password: str, full_name: str, email: str | None = None
):

    existing_user = get_user_by_phone(db, phone)

    if existing_user:
        raise Exception("Phone already exists")

    hashed = hash_password(password)

    user = create_user(
        db=db, phone=phone, hashed_password=hashed, full_name=full_name, email=email
    )

    return user


def authenticate_user(db: Session, phone: str, password: str):

    user = get_user_by_phone(db, phone)

    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    token = create_access_token({"sub": str(user.id)})

    return token
