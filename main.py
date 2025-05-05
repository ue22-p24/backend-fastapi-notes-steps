VERSION = "03b"

from contextlib import asynccontextmanager
from typing import Annotated

import requests

from fastapi import FastAPI
from fastapi import Depends
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from sqlmodel import SQLModel, create_engine
from sqlmodel import Session
from sqlmodel import Field
from sqlmodel import select

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

"""
http :8000/api/notes
"""
@app.get("/api/notes")
def get_notes(session: SessionDep) -> list[Note]:
    notes = session.exec(select(Note)).all()
    return notes

"""
http :8000/api/notes/1
"""
@app.get("/api/notes/{note_id}")
def get_note(note_id: int, session: SessionDep) -> Note | None:
    note = session.get(Note, note_id)
    return note

"""
http :8000/static/css/style.css
"""
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")

"""
http :8000/front/notes
"""
@app.get("/front/notes", response_class=HTMLResponse)
def notes_page(request: Request, session: SessionDep):
    # get the notes through the API, not directly from the database
    base_url = request.url.scheme + "://" + request.url.netloc
    url = base_url + "/api/notes"
    response = requests.get(url)
    if not (200 <= response.status_code < 300):
        raise Exception(f"Error {response.status_code} while getting notes")
    notes = response.json()
    return templates.TemplateResponse(
        request=request,
        name="notes.html.j2",
        context={"notes": notes})
