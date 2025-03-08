import fireo
import time
import sys
from fastapi import FastAPI, Request, Response
import multiprocessing
import threading
import uvicorn

from app.controllers.driver_controller import driver_router
from app.controllers.team_controller import team_router

fireo.connection(from_file="f1-driver-registry-b91545d3ebfc.json")

app = FastAPI(
    title="F1 Driver Registry",
    description="A small FastAPI + FireO demo for F1 drivers & teams",
    version="1.0.0",
)

# Include the controllers
app.include_router(driver_router)
app.include_router(team_router)

@app.get("/")
def read_root(request: Request):
    return {"message": "Welcome to F1 Driver Registry API"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")