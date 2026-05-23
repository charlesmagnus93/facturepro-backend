from sqlalchemy.orm import Session

from app.repositories.client_repository import (
    create_client,
    get_clients,
    get_client_by_id,
    delete_client,
)


def create_new_client(db: Session, user_id: int, payload):
    return create_client(db, user_id, payload)


def list_clients(db: Session, user_id: int):
    return get_clients(db, user_id)


def remove_client(db: Session, client_id: int, user_id: int):

    client = get_client_by_id(db, client_id, user_id)

    if not client:
        raise Exception("Client not found")

    delete_client(db, client)

    return True
