.PHONY: help setup dev dev-bg down build logs shell \
        test test-unit test-integration \
        lint format \
        migrate migrate-create seed db-reset \
        eval clean

help:
@echo ""
@echo "  ResearchIQ — Developer Commands"
@echo "  ──────────────────────────────────────────────"
@echo "  make setup           First-time setup"
@echo "  make dev             Start full stack"
@echo "  make dev-bg          Start stack in background"
@echo "  make down            Stop all containers"
@echo "  make build           Rebuild Docker images"
@echo "  make logs            Tail all logs"
@echo "  make shell           Shell into API container"
@echo ""
@echo "  make test            Full test suite"
@echo "  make test-unit       Unit tests only"
@echo "  make lint            Run all linters"
@echo "  make format          Auto-format code"
@echo ""
@echo "  make migrate         Run DB migrations"
@echo "  make migrate-create  New migration (prompts name)"
@echo "  make seed            Seed dev fixtures"
@echo "  make db-reset        Reset + migrate + seed"
@echo ""
@echo "  make eval            Run evaluation suite"
@echo "  make clean           Remove containers + volumes"
@echo ""

setup:
@echo "→ Setting up ResearchIQ..."
@[ -f .env ] || (cp .env.example .env && echo "  ✓ .env created")
@cd backend && pip install -e ".[dev]" --quiet && echo "  ✓ Python deps installed"
@cd frontend && npm install --silent && echo "  ✓ Node deps installed"
@pre-commit install && echo "  ✓ Pre-commit hooks installed"
@echo "  Done! Run 'make dev' to start."

dev:
docker compose up --build

dev-bg:
docker compose up --build -d
@echo "  API:      http://localhost:8000/docs"
@echo "  Frontend: http://localhost:5173"
@echo "  Qdrant:   http://localhost:6333/dashboard"

down:
docker compose down

build:
docker compose build --no-cache

logs:
docker compose logs -f

shell:
docker compose exec api bash

test:
docker compose exec api pytest tests/ -v --cov=app --cov-report=term-missing

test-unit:
docker compose exec api pytest tests/unit/ -v

test-integration:
docker compose exec api pytest tests/integration/ -v

test-ci:
cd backend && pytest tests/ -v --cov=app --cov-report=xml --cov-fail-under=70

lint:
cd backend && ruff check . && mypy app/ --ignore-missing-imports
cd frontend && npm run lint

format:
cd backend && black . && isort .
cd frontend && npm run format

migrate:
docker compose exec api alembic upgrade head

migrate-create:
@read -p "Migration name: " name; \
docker compose exec api alembic revision --autogenerate -m "$$name"

seed:
docker compose exec api python scripts/seed_data.py

db-reset:
docker compose exec api alembic downgrade base
docker compose exec api alembic upgrade head
docker compose exec api python scripts/seed_data.py

eval:
docker compose exec api python -m evals.run_all

clean:
docker compose down -v --remove-orphans
find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
@echo "✓ Cleaned"
