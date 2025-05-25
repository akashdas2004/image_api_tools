# app/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import bg_removal, enhancer
from app.core.config import settings
import os

app = FastAPI(title="Image Tools API")

# Use centralized CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure static directory exists at startup
@app.on_event("startup")
async def startup_event():
    os.makedirs("app/static", exist_ok=True)

# Register routers
app.include_router(bg_removal.router, prefix="/bg", tags=["Background Removal"])
app.include_router(enhancer.router, prefix="/enhance", tags=["Enhancer"])
