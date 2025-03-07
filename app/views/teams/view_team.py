from nicegui import ui 
from app.views.config import API_BASE
import requests

def team_detail_page(team_id: str):
    ui.label(f"Team Details").classes("text-2xl font-semibold mt-6")

    # Fetch driver info
    r = requests.get(f"{API_BASE}/team/{team_id}")
    if r.status_code == 200:
        t = r.json()
    else:
        ui.label("Error retrieving team data")
        return
    
    # Display driver info
    # Example: You can list them in a column or in fancy boxes, etc.
    with ui.column().classes("gap-2 mt-4"):
        ui.label(f"Name: {t.get('name')}")
        ui.label(f"Year Founded: {t.get('year_founded')}")
        ui.label(f"Total Pole Positions: {d.get('total_pole_positions')}")
        ui.label(f"Total Race Wins: {d.get('total_race_wins')}")
        ui.label(f"Total Constructor Titles: {d.get('total_constructor_titles')}")
        ui.label(f"Finishing Position Previous Season: {d.get('finishing_position_previous_season')}")
        ui.label(f"Fastest Laps: {d.get('total_fastest_laps')}")
        

    # If the user is logged in, show "Edit" and "Delete" buttons
    # In practice, you'd have logic that checks the login status with Firebase
    # or a user token. You can keep it simple: always show it for now or ask in the next step.
    with ui.row().classes("mt-6"):
        ui.button("Edit Team", on_click=lambda: ui.open(f"/team/edit/{team_id}"))
        ui.button("Delete Team", on_click=lambda: delete_driver(team_id))

def delete_driver(driver_id: str):
    # Confirm, then call your backend to delete the driver
    r = requests.delete(f"{API_BASE}/team/{team_id}")
    if r.status_code == 204:
        ui.notify("Team deleted successfully!")
        ui.open("/teams")  # go back to list
    else:
        ui.notify(f"Error deleting team: {r.text}", close_button="OK")