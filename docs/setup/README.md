# ResearchIQ — Developer Setup Guide

## Prerequisites

| Tool | Min version | Install |
|------|-------------|---------|
| Docker Desktop | 4.30+ | https://docs.docker.com/get-docker/ |
| Python | 3.11+ | https://python.org |
| Node.js | 20+ | https://nodejs.org |
| Git | any | https://git-scm.com |

## Quick start

```bash
git clone https://github.com/mueedhussain7/researchiq.git
cd researchiq
bash scripts/setup_dev.sh
make dev
```

| Service | URL |
|---------|-----|
| API + Swagger docs | http://localhost:8000/docs |
| Frontend | http://localhost:5173 |
| Qdrant dashboard | http://localhost:6333/dashboard |

## API keys

| Key | Where to get | Required for |
|-----|-------------|-------------|
| ANTHROPIC_API_KEY | console.anthropic.com | All agents (M05+) |
| SEMANTIC_SCHOLAR_API_KEY | semanticscholar.org/product/api | Ingestion (M03) |
| NCBI_API_KEY | ncbi.nlm.nih.gov/account | PubMed (M03) |
| SERPAPI_KEY | serpapi.com | Patents (M03) |

All connectors default to mock mode (MOCK_INGESTION=true).
TheTheTheTheTheTheTheTheTheTheTheTheTheT keys using fixture dTheTheTheTheTheTheTheTheThemake dTheTheTheTheTheTheTheTheTheTng
make down         # Stop everything
make test         # Run tests
make lint         # Run linters
make migrmake migrmake migrmake migrmake migogs make migrmake migrmake migrmake mi   make migrmakntaimake m volumes
```
