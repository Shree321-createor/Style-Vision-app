from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.dependencies import provide_session
from app.models.designer_note import DesignerNote
from app.schemas.note_schema import (
    DesignerNoteCreate,
    DesignerNoteResponse
)

notes_router = APIRouter()


@notes_router.post(
    "",
    response_model=DesignerNoteResponse
)
def add_designer_note(
    payload: DesignerNoteCreate,
    session: Session = Depends(provide_session)
):

    note = DesignerNote(
        item_id=payload.item_id,
        remark=payload.remark
    )

    session.add(note)
    session.commit()
    session.refresh(note)

    return note


@notes_router.get(
    "/{item_id}",
    response_model=list[DesignerNoteResponse]
)
def fetch_designer_notes(
    item_id: int,
    session: Session = Depends(provide_session)
):

    notes = (
        session.query(DesignerNote)
        .filter(
            DesignerNote.item_id == item_id
        )
        .all()
    )

    return notes
