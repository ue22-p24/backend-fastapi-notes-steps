VERSION = "01b"

from contextlib import asynccontextmanager
from typing import Annotated

from fastapi import FastAPI
from fastapi import Depends

from sqlmodel import SQLModel, create_engine
from sqlmodel import Session

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


# Create the FastAPI app with the lifespan context manager
app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    return dict(message="Hello FastAPI World!",
                version=VERSION)
