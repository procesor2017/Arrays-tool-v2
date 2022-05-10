from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from matrix.create_matrix import choose_and_return_matrix

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"Hello": "World"}

@app.get("/getTable")
def get_table(user_input: list):
    return choose_and_return_matrix(user_input)