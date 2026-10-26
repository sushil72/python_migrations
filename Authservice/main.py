from fastapi import FastAPI

from Authservice.api.v1.router import api_router
from Authservice.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description="Auth service rebuilt in Python FastAPI.",
    )
    app.include_router(api_router, prefix=settings.API_V1_PREFIX)
    return app


app = create_app()
