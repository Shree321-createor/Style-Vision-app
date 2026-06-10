from pydantic import BaseModel


class ClothingItemResponse(BaseModel):

    id: int

    image_path: str

    description: str

    garment_type: str

    style: str

    material: str

    color_palette: str

    pattern: str

    season: str

    occasion: str

    consumer_profile: str

    trend_notes: str

    continent: str

    country: str

    city: str

    class Config:
        from_attributes = True
