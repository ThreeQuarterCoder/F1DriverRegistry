from nicegui import ui 
from app.views.config import API_BASE
import requests

def team_list_page():
    ui.label("All Teams").classes("text-2xl font-semibold mt-6")

    response = requests.get(f"{API_BASE}/teams")
    if response.status_code == 200:
        teams = response.json()  # Suppose it returns a list of teams
    else:
        ui.label(f"Error fetching drivers: {response.text}")
        return
    
    with ui.column().classes("mt-4"):
        for t in teams:
            with ui.row():
                team_name = t.name
                team_id = t.id
                page_link = ui.link(text=team_name, target=ui.navigate.to(f"/team/{team_id}"), new_tab=False)
                
