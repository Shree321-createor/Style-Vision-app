from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

DB_CONNECTION_URL = "sqlite:///catalog.db"

db_engine = create_engine(
    DB_CONNECTION_URL,
    connect_args={"check_same_thread": False}
)

DbSession = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=db_engine
)

EntityBase = declarative_base()
