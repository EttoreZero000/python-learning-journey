from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from src.projects.stardew_manager_1.backend.state import global_lotes
from src.projects.stardew_manager_1.backend.domain import lote

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Modelo para recibir JSON desde frontend
class CreateLote(BaseModel):
    name: str
    length: int
    days: int


@app.post("/lote")
def create_lote(data: CreateLote):
    nuevo = lote(name=data.name, length=data.length, days=data.days)
    global_lotes.create(nuevo)
    return {"status": "ok"}


@app.get("/lotes/growing")
def get_growing():
    return [
        {"name": l.name, "length": l.length, "days": l.days}
        for l in global_lotes.viewGrowing()
    ]


@app.get("/lotes/ready")
def get_ready():
    return [
        {"name": l.name, "length": l.length}
        for l in global_lotes.viewReady()
    ]


@app.post("/day")
def pass_day():
    global_lotes.passDay()
    return {"status": "day passed"}


@app.post("/harvest/{index}")
def harvest(index: int):
    harvested = global_lotes.harvest(index)
    return {"harvested": {"name": harvested.name, "length": harvested.length}}
