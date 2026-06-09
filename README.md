<div align="center">

# ResearchIQ

### AI-Powered Research Intelligence Platform

*Impact Assessment · Citation Validation · Gap Detection · Innovation Discovery*

[![CI](https://github.com/mueedhussain7/researchiq/actions/workflows/ci.yml/badge.svg)](https://github.com/mueedhussain7/researchiq/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue?logo=python)](https://python.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.5+-blue?logo=typescript)](https://typescriptlang.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green?logo=fastapi)](https://fastapi.tiangolo.com)

</div>

---

## What is ResearchIQ?

ResearchIQ is a production-grade multi-agent AI platform for researchers,
universities, and R&D teams. Submit a research topic or paper and get back:

- **Research Impact Assessment** — citation trajectory, influence score, cross-domain spread
- **Citation Validation** — verify that citations actually support the claims that use them
- **Research Gap Detection** — identify underexplored areas and open questions
- **Innovation Discovery** — find commercially valuable opportunities from research and patent trends

## Quick Start

```bash
git clone https://github.com/mueedhussain7/researchiq.git
cd researchiq
bash scripts/setup_dev.sh
make dev
```

- API docs:  http://localhost:8000/docs
- Frontend:  http://localhost:5173
- Qdrant:    http://localhost:6333/dashboard

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | React 18, TypeScript, Tailwind CSS, Vite |
| Backend | FastAPI, Python 3.11, Pydantic v2 |
| Database | PostgreSQL 16, SQLAlchemy 2, Alembic |
| Queue | Celery + Redis 7 |
| Vector DB | Qdrant |
| AI Agents | CrewAI + LangChain + Anthropic Claude |
| Embeddings | sentence-transformers (local) |
| Infra | Docker, GitHub Actions, AWS, Terraform |

## License

MIT
