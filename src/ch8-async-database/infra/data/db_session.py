from pathlib import Path
from typing import Callable, Optional

import sqlalchemy as sa
from sqlalchemy.ext.asyncio.engine import create_async_engine
from sqlalchemy.ext.asyncio.session import AsyncSession
import sqlalchemy.orm as orm
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import Session

from app.models.base.BaseModel import BaseModel

__factory: Optional[Callable[[], Session]] = None
__async_engine: Optional[AsyncEngine] = None

def global_init(db_file: str):
    global __factory, __async_engine

    # If we already have done the setup, we do not do it a second time
    # The Job of the factory is to provide the sessions for unit of works
    if __factory:
        return

    db_file = str(db_file).strip()

    if not db_file:
        raise Exception("You must specify a db file.")

    folder = Path(db_file).parent
    folder.mkdir(parents=True, exist_ok=True)

    conn_str_sync = 'sqlite:///' + db_file
    conn_str_async = 'sqlite+aiosqlite:///' + db_file
    
    # Adding check_same_thread = False after the recording. This can be an issue about
    # creating / owner thread when cleaning up sessions, etc. This is a sqlite restriction
    # that we probably don't care about in this example.
    engine = sa.create_engine(conn_str_sync, echo=False, connect_args={"check_same_thread": False})
    __async_engine = create_async_engine(conn_str_async, echo=False, connect_args={"check_same_thread": False})
    __factory = orm.sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    import app.models.__all_models

    BaseModel.metadata.create_all(engine)


def create_session() -> Session:
    if not __factory:
        raise Exception("You must call global_init() before using this method.")

    session: Session = __factory()
    session.expire_on_commit = False

    return session

def create_async_session() -> AsyncSession:
    if not __async_engine:
        raise Exception("You must call global_init() before using this method.")

    session: AsyncSession = AsyncSession(__async_engine)
    session.sync_session.expire_on_commit = False
    
    return session


