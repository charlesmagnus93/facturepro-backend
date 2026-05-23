from sqlalchemy import Column, Integer, String, ForeignKey

from sqlalchemy.orm import relationship

from app.db.database import Base


class Client(Base):
    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    phone = Column(String, nullable=True)

    email = Column(String, nullable=True)

    address = Column(String, nullable=True)

    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="clients")
