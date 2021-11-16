from pathlib import Path
from typing import Callable, Optional

import sqlalchemy as sa
import sqlalchemy.orm as orm
from sqlalchemy.orm import Session

from app.models.base.BaseModel import BaseModel

__factory: Optional[Callable[[], Session]] = None


def global_init(db_file: str):
    global __factory

    # If we already have done the setup, we do not do it a second time
    # The Job of the factory is to provide the sessions for unit of works
    if __factory:
        return

    db_file = str(db_file).strip()

    if not db_file:
        raise Exception("You must specify a db file.")

    folder = Path(db_file).parent
    folder.mkdir(parents=True, exist_ok=True)

    conn_str = 'sqlite:///' + db_file
    print("Connecting to DB with {}".format(conn_str))

    # Adding check_same_thread = False after the recording. This can be an issue about
    # creating / owner thread when cleaning up sessions, etc. This is a sqlite restriction
    # that we probably don't care about in this example.
    engine = sa.create_engine(conn_str, echo=False, connect_args={"check_same_thread": False})
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

