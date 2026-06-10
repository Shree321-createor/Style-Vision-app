from app.database.db import DbSession


def provide_session():
    session = DbSession()

    try:
        yield session

    finally:
        session.close()
