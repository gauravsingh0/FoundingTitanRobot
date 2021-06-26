from SaitamaRobot import DB_URI, LOGGER

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session



def start() -> scoped_session:
    engine = create_engine(DB_URI, client_encoding="utf8")
    log.info("[PostgreSQL] Connecting to ElephantSQL database......")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
try:
    SESSION = start()
except Exception as e:
    log.exception(f'[PostgreSQL] Failed to connect to the database due to {e}')
    exit()
   
log.info("[PostgreSQL] Connection to ElephantSQL successful, session started.")
