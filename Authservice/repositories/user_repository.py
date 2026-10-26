from sqlalchemy import select
from sqlalchemy.orm import Session

from Authservice.models.user import User
from python_migrations.Authservice.schemas.requests import RegisterRequest


class UserRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def get_by_email(self, email: str) -> User | None:
        statement = select(User).where(User.email == email)
        return self.db.scalars(statement).first()

    def create(self, payload: RegisterRequest, hashed_password: str) -> User:
        user = User(
            email=payload.email,
            full_name=payload.full_name,
            hashed_password=hashed_password,
        )
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
