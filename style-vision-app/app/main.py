from fastapi import FastAPI

from app.database.db import EntityBase
from app.database.db import db_engine

from app.models.clothing import ClothingItem
from app.models.designer_note import DesignerNote

from app.api.routes.catalog import catalog_router
from app.api.routes.notes import notes_router

from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Style Vision Catalog API",
    version="1.0.0"
)

app.mount(
    "/uploads",
    StaticFiles(directory="uploads"),
    name="uploads"
)

app.include_router(
    catalog_router,
    prefix="/items",
    tags=["Catalog"]
)

app.include_router(
    notes_router,
    prefix="/notes",
    tags=["Designer Notes"]
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

EntityBase.metadata.create_all(bind=db_engine)


@app.get("/health")
def ping():
    return {
        "status": "running"
    }
