from fastapi import APIRouter, Depends, HTTPException

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.models.user import User

from app.core.dependencies import get_current_user

from app.schemas.client import ClientCreate, ClientResponse

from app.services.client_service import create_new_client, list_clients, remove_client

router = APIRouter(prefix="/clients", tags=["Clients"])


@router.post("/", response_model=ClientResponse)
def create(
    payload: ClientCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    client = create_new_client(db=db, user_id=current_user.id, payload=payload)

    return client


@router.get("/", response_model=list[ClientResponse])
def get_all(
    db: Session = Depends(get_db), current_user: User = Depends(get_current_user)
):

    return list_clients(db, current_user.id)


@router.delete("/{client_id}")
def delete(
    client_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):

    try:

        remove_client(db, client_id, current_user.id)

        return {"message": "Client deleted"}

    except Exception as e:

        raise HTTPException(status_code=404, detail=str(e))
