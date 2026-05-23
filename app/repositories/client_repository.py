from sqlalchemy.orm import Session

from app.models.client import Client


def create_client(db: Session, user_id: int, payload):

    client = Client(
        name=payload.name,
        phone=payload.phone,
        email=payload.email,
        address=payload.address,
        user_id=user_id,
    )

    db.add(client)
    db.commit()
    db.refresh(client)

    return client


def get_clients(db: Session, user_id: int):

    return db.query(Client).filter(Client.user_id == user_id).all()


def get_client_by_id(db: Session, client_id: int, user_id: int):

    return (
        db.query(Client)
        .filter(Client.id == client_id, Client.user_id == user_id)
        .first()
    )


def delete_client(db: Session, client):

    db.delete(client)
    db.commit()

    return True
