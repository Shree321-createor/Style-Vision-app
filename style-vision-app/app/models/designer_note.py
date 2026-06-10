from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import ForeignKey

from app.database.db import EntityBase


class DesignerNote(EntityBase):
    __tablename__ = "designer_notes"

    id = Column(Integer, primary_key=True)

    item_id = Column(
        Integer,
        ForeignKey("clothing_items.id")
    )

    remark = Column(Text)
