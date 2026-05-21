from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel

# Modules
from libs.status import get_status
from libs.preview import get_preview
from libs.record import record
from libs.record import stop_record

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class Experiment(BaseModel):
    name: str

@app.get("/status")
def status():
    return get_status()

@app.get("/preview")
def status():
    return get_preview()

@app.post("/start_record")
def start_recording(experiment: Experiment):
    return record(experiment.name)

@app.post("/stop_record")
def stop_recording(experiment: Experiment):
    return stop_record(experiment.name)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
