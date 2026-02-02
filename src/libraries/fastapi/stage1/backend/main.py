from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 👈 permite cualquier origen (solo para desarrollo)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/users")
def get_users():
    return [
        {"id": 1, "name": "Ana"},
        {"id": 2, "name": "Luis"}
    ]
