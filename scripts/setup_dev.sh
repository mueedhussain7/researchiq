#!/usr/bin/env bash
#  ResearchIQ — One-command developer setup
#  Usage: bash scripts/setup_dev.sh
set -euo pipefail

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

info() { echo -e "${GREEN}→${NC} $1"; }
warn() { echo -e "${YELLOW}⚠${NC}  $1"; }
ok()   { echo -e "${GREEN}✓${NC}  $1"; }
err()  { echo -e "${RED}✗${NC}  $1"; exit 1; }

echo ""
echo "  ResearchIQ — Developer Setup"
echo "  ──────────────────────────────────────"
echo ""

# Check prerequisites
info "Checking prerequisites..."

command -v docker  >/dev/null 2>&1 || err "Docker not found. Install from https://docs.docker.com/get-docker/"
command -v python3 >/dev/null 2>&1 || err "Python 3 not found. Install from https://python.org"
command -v node    >/dev/null 2>&1 || err "Node.js not found. Install from https://nodejs.org"
command -v git     >/dev/null 2>&1 || err "Git not found."

ok "Docker  $(docker --version | cut -d' ' -f3)"
ok "Python  $(python3 --version | cut -d' ' -f2)"
ok "Node    $(node --version)"

# Environment file
info "Setting up environment file..."

if [ ! -f .env ]; then
    cp .env.example .env
    ok ".env created from .env.example"
    warn "Open .env and add your ANTHROPIC_API_KEY before running agents"
else
    ok ".env already exists — skipping"
fi

# Python dependencies 
info "Installing Python dependencies..."
cd backend
pip install -e ".[dev]" -q
cd ..
ok "Python dependencies installed"

# Node dependencies 
info "Installing Node.js dependencies..."
cd frontend
npm install --silent
cd ..
ok "Node.js dependencies installed"

# Pre-commit hooks
info "Installing pre-commit hooks..."
pre-commit install
ok "Pre-commit hooks installed"

# Start Docker services 
info "Starting infrastructure services..."
docker compose up -d postgres redis qdrant
echo "  Waiting 10 seconds for services to be ready..."
sleep 10

# Health checks
info "Checking service health..."

docker compose exec -T postgres pg_isready -U researchiq -q \
    && ok "PostgreSQL is ready" \
    || warn "PostgreSQL is still starting — wait a moment then run make dev"

docker compose exec -T redis redis-cli ping | grep -q PONG \
    && ok "Redis is ready" \
    || warn "Redis is still starting"

curl -sf http://localhost:6333/healthz >/dev/null \
    && ok "Qdrant is ready" \
    || warn "Qdrant is still starting"

echo ""
echo "  ──────────────────────────────────────"
echo "  Setup complete. Next steps:"
echo ""
echo "  1. Add your ANTHROPIC_API_KEY to .env"
echo "  2. Run:  make dev"
echo "  3. API:  http://localhost:8000/docs"
echo "  4. UI:   http://localhost:5173"
echo "  ──────────────────────────────────────"
echo ""

chmod +x scripts/setup_dev.sh
