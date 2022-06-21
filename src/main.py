from fastapi import FastAPI, Request
#from fastapi.middleware.cors import CORSMiddleware
# Funkční
from .modules.create_matrix import choose_and_return_matrix
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import logging

app = FastAPI(debug=True)
logger = logging.getLogger("uvicorn")

app.mount("/static", StaticFiles(directory="./src/static"), name="static")

template = Jinja2Templates(directory="./src/templates")


class Input(BaseModel):
    data: list

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return template.TemplateResponse("index.html", {"request": request})

@app.get("/cs", response_class=HTMLResponse)
def home(request: Request):
    return template.TemplateResponse("index_cs.html", {"request": request})

@app.post("/getInformation")
async def getInformation(input: Input):
    a = jsonable_encoder(input)
    return choose_and_return_matrix(a["data"])


