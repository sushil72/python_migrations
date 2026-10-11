# Python Auth Service

FastAPI version of an auth service, structured for learning and later growth.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python -m app.db.init_db
uvicorn main:app --reload
```

Open:

- API docs: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/api/v1/health

## Current endpoints

- `POST /api/v1/auth/register`
- `POST /api/v1/auth/login`

## Project layout

```text
app/
  api/             FastAPI routers and dependencies
  core/            Settings and security utilities
  db/              SQLAlchemy engine, session, and database init
  models/          Database models
  repositories/    Database access layer
  schemas/         Pydantic request and response models
  services/        Business logic
tests/             Test files
```
