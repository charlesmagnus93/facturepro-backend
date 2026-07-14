from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.invoice import Invoice


def generate_invoice_number(db: Session, user_id: int) -> str:
    count = db.query(func.count(Invoice.id)).filter(
        Invoice.user_id == user_id
    ).scalar() or 0

    next_number = count + 1
    return f"FAC-{next_number:05d}"
