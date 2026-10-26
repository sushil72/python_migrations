from collections.abc import Generator

from fastapi import Depends
from sqlalchemy.orm import Session

from Authservice.db.session import SessionLocal
from Authservice.repositories.user_repository import UserRepository
from Authservice.services.auth_service import AuthService


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_auth_service(db: Session = Depends(get_db)) -> AuthService:
    return AuthService(user_repository=UserRepository(db))
