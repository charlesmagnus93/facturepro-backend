from fastapi import APIRouter, Depends, HTTPException, Request, status

from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from app.db.session import get_db

from app.schemas.auth import UserCreate, UserLogin, Token

from app.services.auth_service import register_user, authenticate_user

from app.core.rate_limit import login_limiter, get_client_ip

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register(payload: UserCreate, db: Session = Depends(get_db)):
    from app.core.logging import logger

    try:
        user = register_user(
            db=db,
            phone=payload.phone,
            password=payload.password,
            full_name=payload.full_name,
            email=payload.email,
        )

        logger.info(f"New user registered: {user.phone}")
        return {"message": "User created", "phone": user.phone}

    except Exception as e:
        logger.warning(f"Registration failed: {e}")
        raise HTTPException(
            status_code=400,
            detail="Impossible de créer le compte. Ce numéro est peut-être déjà utilisé.",
        )


@router.post("/login", response_model=Token)
async def login(
    request: Request,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    client_ip = await get_client_ip(request)
    login_limiter.check(client_ip)

    token = authenticate_user(db=db, phone=form_data.username, password=form_data.password)

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials"
        )

    return {"access_token": token, "token_type": "bearer"}
