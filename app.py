from pkgfile import *

from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()


@app.get("/api")
async def read_item(f: str):
    return run(f)


@app.get("/")
async def index():
    return FileResponse("web/index.html")


app.mount("/", StaticFiles(directory="web"), name="web")
