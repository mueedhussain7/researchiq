"""
ResearchIQ — FastAPI application entry point.

Responsibilities:
- Creates the app instance with metadata
- Registers CORS and request-ID middleware
- Exposes /health and / endpoints
- Will mount all API routers (added in Milestone 2)
"""
import uuid
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.core.logging import configure_logging, get_logger

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Startup and shutdown lifecycle."""
    configure_logging(settings.LOG_LEVEL)
    logger.info(
        "researchiq_startup",
        env=settings.APP_ENV,
        version=settings.APP_VERSION,
        mock_ingestion=settings.MOCK_INGESTION,
    )
    yield
    logger.info("researchiq_shutdown")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description=(
        "AI-powered research intelligence: impact assessment, "
        "citation validation, gap detection, and innovation discovery."
    ),
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    lifespan=lifespan,
)

# ── Middleware ─────────────────────────────────────────────────

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_request_id(request: Request, call_next):
    """Attach a short unique ID to every request for tracing."""
    request_id = str(uuid.uuid4())[:8]
    request.state.request_id = request_id
    response = await call_next(request)
    response.headers["X-Request-ID"] = request_id
    return response


# ── Endpoints ──────────────────────────────────────────────────

@app.get("/health", tags=["system"])
async def health_check():
    """
    Health probe used by Docker, load balancers, and CI.
    Returns 200 when the API process is running.
    """
    return JSONResponse({
        "status": "healthy",
        "app": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "env": settings.APP_ENV,
    })


@app.get("/", tags=["system"])
async def root():
    """Welcome message with links to docs and health."""
    return {
        "message": f"Welcome to {settings.APP_NAME} API",
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "health": "/health",
    }


# ── Routers (uncommented in Milestone 2) ──────────────────────
# from app.api.v1.endpoints import auth, analyses, search
# app.include_router(auth.router,     prefix=settings.API_PREFIX)
# app.include_router(analyses.router, prefix=settings.API_PREFIX)
# app.include_router(search.router,   prefix=settings.API_PREFIX)
