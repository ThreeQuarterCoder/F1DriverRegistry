import fireo
import threading
import uvicorn
from nicegui import ui
from fastapi import FastAPI, Request, Response
from queue import Queue

# Import the routers from controllers
from app.controllers.driver_controller import driver_router
from app.controllers.team_controller import team_router
from app.controllers.view_controller import register_view_routes

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

# If you have an auth system, define or import it here:
# from auth import auth_required
# etc.

@app.get("/")
def read_root(request: Request):
    return {"message": "Welcome to F1 Driver Registry API"}

register_view_routes()

command_queue = Queue()

def run_uvicorn():
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="debug")


def run_nicegui():
    ui.run(title="F1 Registry", host="127.0.0.1", port=8001)

def command_listener():
    """Listen for user commands and handle them."""
    while True:
        command = input("Enter command (q=quit, r=restart, s=status): ").strip().lower()
        command_queue.put(command)
        if command == "q":
            break

# def run_parallel():
#     app_thread = threading.Thread(target=run_uvicorn)
#     app_thread.start()
#     run_nicegui()

def run_parallel():
    """Run both servers in parallel with command handling."""
    while True:
        global api_thread, ui_thread
        
        # Start API server thread
        api_thread = threading.Thread(target=run_uvicorn, daemon=True)
        api_thread.start()
        
        # Start UI server thread
        ui_thread = threading.Thread(target=run_nicegui, daemon=True)
        ui_thread.start()
        
        # Start command listener thread (not daemon to keep the main loop active)
        command_thread = threading.Thread(target=command_listener)
        command_thread.start()
        
        # Process commands
        while True:
            command = command_queue.get()
            
            if command == "q":
                print("Shutting down servers...")
                break
            elif command == "r":
                print("Restarting servers...")
                api_thread.join(timeout=1)  # Attempt to stop thread
                ui_thread.join(timeout=1)   # Attempt to stop thread
                break  # Break out to restart servers
            elif command == "s":
                print("API Server: Running" if api_thread.is_alive() else "API Server: Stopped")
                print("UI Server: Running" if ui_thread.is_alive() else "UI Server: Stopped")
        
        if command == "q":
            sys.exit(0)
        
        # Short delay before restarting to avoid excessive CPU usage
        time.sleep(2)
        print("Restarting...")

# if __name__ in {"__main__", "__mp_main__"}:
#     run_parallel()


if __name__ in {"__main__",  "__mp_main__"}:
    run_parallel()