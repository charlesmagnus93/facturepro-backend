from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Optional
from sqlalchemy.orm import Session

from app.models.user import User
from app.core.dependencies import get_current_user
from app.db.session import get_db

router = APIRouter(prefix="/users", tags=["Users"])


class CompanyProfileUpdate(BaseModel):
    company_name: Optional[str] = None
    company_address: Optional[str] = None
    company_phone: Optional[str] = None
    company_email: Optional[str] = None
    company_logo_url: Optional[str] = None


@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "phone": current_user.phone,
        "email": current_user.email,
        "full_name": current_user.full_name,
        "company_name": current_user.company_name,
        "company_address": current_user.company_address,
        "company_phone": current_user.company_phone,
        "company_email": current_user.company_email,
        "company_logo_url": current_user.company_logo_url,
    }


@router.put("/me/company")
def update_company_profile(
    payload: CompanyProfileUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    if payload.company_name is not None:
        current_user.company_name = payload.company_name
    if payload.company_address is not None:
        current_user.company_address = payload.company_address
    if payload.company_phone is not None:
        current_user.company_phone = payload.company_phone
    if payload.company_email is not None:
        current_user.company_email = payload.company_email
    if payload.company_logo_url is not None:
        current_user.company_logo_url = payload.company_logo_url

    db.commit()
    db.refresh(current_user)

    return {
        "message": "Profil entreprise mis à jour",
        "company_name": current_user.company_name,
        "company_address": current_user.company_address,
        "company_phone": current_user.company_phone,
        "company_email": current_user.company_email,
        "company_logo_url": current_user.company_logo_url,
    }