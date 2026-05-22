from fastapi import APIRouter, Depends, HTTPException, status

from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.schemas.auth import UserCreate, UserLogin, Token

from app.services.auth_service import register_user, authenticate_user

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register(payload: UserCreate, db: Session = Depends(get_db)):

    try:
        user = register_user(
            db=db,
            phone=payload.phone,
            password=payload.password,
            full_name=payload.full_name,
            email=payload.email,
        )

        return {"message": "User created", "phone": user.phone}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=Token)
def login(payload: UserLogin, db: Session = Depends(get_db)):

    token = authenticate_user(db=db, phone=payload.phone, password=payload.password)

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    return {"access_token": token, "token_type": "bearer"}
