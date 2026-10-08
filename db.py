from typing import Annotated, Depends

from sqlmodel import Session, create_engine

sqlite_name = "db.sqilte3"
sqlite_url = f"sqlite///{sqlite_name}"

engine = create_engine(sqlite_url)

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
