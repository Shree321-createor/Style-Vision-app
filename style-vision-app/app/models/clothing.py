from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from app.database.db import EntityBase


class ClothingItem(EntityBase):
    __tablename__ = "clothing_items"

    id = Column(Integer, primary_key=True)

    image_path = Column("file_path", String)

    description = Column("caption", Text)

    garment_type = Column("clothing_type", String)

    style = Column("look", String)

    material = Column("fabric", String)

    color_palette = Column("color_tones", String)

    pattern = Column("design_pattern", String)

    season = Column("suitable_season", String)

    occasion = Column("wear_occasion", String)

    consumer_profile = Column("target_audience", String)

    trend_notes = Column("fashion_trend", Text)

    continent = Column("region", String)

    country = Column("nation", String)

    city = Column("locale", String)
