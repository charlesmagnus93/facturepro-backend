from sqlalchemy.orm import Session

from app.models.user import User


def get_user_by_phone(db: Session, phone: str):
    return db.query(User).filter(User.phone == phone).first()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create_user(
    db: Session,
    phone: str,
    hashed_password: str,
    full_name: str,
    email: str | None = None,
):

    user = User(
        phone=phone, email=email, hashed_password=hashed_password, full_name=full_name
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def update_invoice(db: Session, invoice):

    db.commit()
    db.refresh(invoice)

    return invoice
