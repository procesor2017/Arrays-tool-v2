from fastapi import FastAPI, Request
#from fastapi.middleware.cors import CORSMiddleware
# Funkční
from .modules.create_matrix import choose_and_return_matrix
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

app = FastAPI()

"""
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
"""

class Input(BaseModel):
    data: list

@app.get("/")
def home():
    return {"Hello": "World"}

@app.post("/getInformation")
async def getInformation(input: Input):
    a = jsonable_encoder(input)
    return choose_and_return_matrix(a["data"])


