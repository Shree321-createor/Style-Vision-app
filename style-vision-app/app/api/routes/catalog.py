from pathlib import Path
import shutil
from sqlalchemy import or_

from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File
from fastapi import Depends
from fastapi import Query
from typing import List

from sqlalchemy.orm import Session

from app.database.dependencies import provide_session
from app.models.clothing import ClothingItem
from app.services.style_analysis_service import StyleAnalysisService
from app.schemas.clothing_schema import ClothingItemResponse
from app.models.designer_note import DesignerNote


catalog_router = APIRouter()
STORAGE_FOLDER = "uploads"
Path(STORAGE_FOLDER).mkdir(exist_ok=True)

style_service = StyleAnalysisService()


@catalog_router.post("/upload")
async def upload_clothing_image(
    image: UploadFile = File(...),
    session: Session = Depends(provide_session)
):

    destination = f"{STORAGE_FOLDER}/{image.filename}"

    with open(destination, "wb") as buf:
        shutil.copyfileobj(
            image.file,
            buf
        )

    attributes = style_service.analyze(destination)

    item = ClothingItem(
        image_path=destination,
        description=attributes["description"],
        garment_type=attributes["garment_type"],
        style=attributes["style"],
        material=attributes["material"],
        color_palette=attributes["color_palette"],
        pattern=attributes["pattern"],
        season=attributes["season"],
        occasion=attributes["occasion"],
        consumer_profile=attributes["consumer_profile"],
        trend_notes=attributes["trend_notes"],
        continent=attributes["continent"],
        country=attributes["country"],
        city=attributes["city"]
    )

    session.add(item)
    session.commit()
    session.refresh(item)

    return item


@catalog_router.get(
    "",
    response_model=List[ClothingItemResponse]
)
def list_clothing_items(
    session: Session = Depends(provide_session)
):

    items = session.query(ClothingItem).all()

    return items


@catalog_router.get("/filters")
def get_available_filters(
    session: Session = Depends(provide_session)
):

    garment_types = [
        row[0]
        for row in session.query(
            ClothingItem.garment_type
        ).distinct().all()
    ]

    styles = [
        row[0]
        for row in session.query(
            ClothingItem.style
        ).distinct().all()
    ]

    materials = [
        row[0]
        for row in session.query(
            ClothingItem.material
        ).distinct().all()
    ]

    seasons = [
        row[0]
        for row in session.query(
            ClothingItem.season
        ).distinct().all()
    ]

    return {
        "garment_types": garment_types,
        "styles": styles,
        "materials": materials,
        "seasons": seasons
    }


@catalog_router.get(
    "/filter",
    response_model=List[ClothingItemResponse]
)
def filter_clothing_items(
    garment_type: str | None = Query(None),
    style: str | None = Query(None),
    season: str | None = Query(None),
    session: Session = Depends(provide_session)
):

    query = session.query(ClothingItem)

    if garment_type:
        query = query.filter(
            ClothingItem.garment_type == garment_type
        )

    if style:
        query = query.filter(
            ClothingItem.style == style
        )

    if season:
        query = query.filter(
            ClothingItem.season == season
        )

    return query.all()


@catalog_router.get(
    "/search",
    response_model=List[ClothingItemResponse]
)
def search_clothing_items(
    q: str,
    session: Session = Depends(provide_session)
):

    results = (
        session.query(ClothingItem)
        .filter(
            or_(
                ClothingItem.description.ilike(f"%{q}%"),
                ClothingItem.garment_type.ilike(f"%{q}%"),
                ClothingItem.style.ilike(f"%{q}%"),
                ClothingItem.material.ilike(f"%{q}%"),
                ClothingItem.pattern.ilike(f"%{q}%"),
                ClothingItem.occasion.ilike(f"%{q}%")
            )
        )
        .all()
    )

    return results
