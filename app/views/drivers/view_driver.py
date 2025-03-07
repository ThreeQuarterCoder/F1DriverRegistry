from nicegui import ui 
from app.views.config import API_BASE
import requests

def driver_detail_page(driver_id: str):
    ui.label(f"Driver Details").classes("text-2xl font-semibold mt-6")

    # Fetch driver info
    r = requests.get(f"{API_BASE}/drivers/{driver_id}")
    if r.status_code == 200:
        d = r.json()
    else:
        ui.label("Error retrieving driver data")
        return
    
    # Display driver info
    # Example: You can list them in a column or in fancy boxes, etc.
    with ui.column().classes("gap-2 mt-4"):
        ui.label(f"Name: {d.get('name')}")
        ui.label(f"Age: {d.get('age')}")
        ui.label(f"Total Pole Positions: {d.get('total_pole_positions')}")
        ui.label(f"Total Race Wins: {d.get('total_race_wins')}")
        ui.label(f"Total Points Scored: {d.get('total_points_scored')}")
        ui.label(f"World Titles: {d.get('total_world_titles')}")
        ui.label(f"Fastest Laps: {d.get('total_fastest_laps')}")
        #ui.label(f"Team: {d.get('team_name')}")
        # or however you store that

    # If the user is logged in, show "Edit" and "Delete" buttons
    # In practice, you'd have logic that checks the login status with Firebase
    # or a user token. You can keep it simple: always show it for now or ask in the next step.
    with ui.row().classes("mt-6"):
        ui.button("Edit Driver", on_click=lambda: ui.open(f"/driver/edit/{driver_id}"))
        ui.button("Delete Driver", on_click=lambda: delete_driver(driver_id))

def delete_driver(driver_id: str):
    # Confirm, then call your backend to delete the driver
    r = requests.delete(f"{API_BASE}/drivers/{driver_id}")
    if r.status_code == 204:
        ui.notify("Driver deleted successfully!")
        ui.open("/drivers")  # go back to list
    else:
        ui.notify(f"Error deleting driver: {r.text}", close_button="OK")