from Authservice.core.security import create_access_token, hash_password, verify_password
from Authservice.models.user import User
from Authservice.repositories.user_repository import UserRepository
from python_migrations.Authservice.schemas.requests import LoginRequest, RegisterRequest
from python_migrations.Authservice.schemas.response import TokenResponse


class AuthService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository

    def register(self, payload: RegisterRequest) -> User | None:
        existing_user = self.user_repository.get_by_email(payload.email)
        if existing_user is not None:
            return None

        hashed_password = hash_password(payload.password)
        return self.user_repository.create(payload, hashed_password)

    def login(self, payload: LoginRequest) -> TokenResponse | None:
        user = self.user_repository.get_by_email(payload.email)
        if user is None or not verify_password(payload.password, user.hashed_password):
            return None

        access_token = create_access_token(subject=user.email)
        return TokenResponse(access_token=access_token)
