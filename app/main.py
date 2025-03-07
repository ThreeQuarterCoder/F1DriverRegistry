import fireo
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

# Import the routers from controllers
from app.controllers.driver_controller import driver_router
from app.controllers.team_controller import team_router

# Initialize FireO here OR in models.py
fireo.connection(from_file="f1-driver-registry-b91545d3ebfc.json")

app = FastAPI(
    title="F1 Driver Registry",
    description="A small FastAPI + FireO demo for F1 drivers & teams",
    version="1.0.0",
)

# Include the controllers
app.include_router(driver_router)
app.include_router(team_router)

templates = Jinja2Templates(directory="app/templates")

# If you have an auth system, define or import it here:
# from auth import auth_required
# etc.

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Welcome to the F1 Driver Registry Aplication"})