VERSION = "02a"

from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI
from fastapi import Depends

from sqlmodel import SQLModel, create_engine
from sqlmodel import Session
from sqlmodel import Field

SQLITE_URL = f"sqlite:///notes.db"
engine = create_engine(SQLITE_URL)

# this is how we control what is done at startup and shutdown
@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup logic comes here
    # Create the database and tables if they don't exist
    SQLModel.metadata.create_all(engine)

    yield
    # shutdown logic comes here
    # none so far


# create a so-called "dependency" to get the database session
def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]


class Note(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    done: bool = False


# Create the FastAPI app with the lifespan context manager
app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return dict(message="Hello FastAPI World!",
                version=VERSION)

"""
http :8000/api/notes title="Devoirs" description="TP Backend"
http :8000/api/notes title="Papiers" description="Nouveau Passeport"
http :8000/api/notes title="Dentiste" description="ouille !" done:=true
"""
@app.post("/api/notes")
def create_note(note: Note, session: SessionDep) -> Note:
    session.add(note)
    session.commit()
    session.refresh(note)
    return note
