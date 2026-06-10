from pydantic import BaseModel


class DesignerNoteCreate(BaseModel):
    item_id: int
    remark: str


class DesignerNoteResponse(BaseModel):
    id: int
    item_id: int
    remark: str

    class Config:
        from_attributes = True
