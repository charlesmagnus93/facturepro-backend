# FacturePro Backend

Backend API for FacturePro SaaS.

## Stack

- FastAPI
- PostgreSQL
- SQLAlchemy

## Run

```bash
uvicorn app.main:app --reload
```

## Database migrations

Create migration:

```bash
alembic revision --autogenerate -m "message"
```

Appliquer migration:

```bash
alembic upgrade head
```

Voir historique migrations:

```bash
alembic history
```

Revenir en arrière:

```bash
alembic downgrade base
```
