from Authservice.db.base import Base
from Authservice.db.session import engine
from Authservice.models import User


def init_db() -> None:
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
