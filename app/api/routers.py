"""This module includes API routers."""
from fastapi import APIRouter
from .endpoints.FAQ_RAG import router as perf_router
router = APIRouter()

# Routers from each endpoint
router.include_router(perf_router)
