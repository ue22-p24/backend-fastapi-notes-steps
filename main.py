VERSION = "00"

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return dict(message="Hello FastAPI World!",
                version=VERSION)
