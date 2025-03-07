from nicegui import ui 
from app.views.config import API_BASE
import requests

def driver_list_page():
    ui.label("All Drivers").classes("text-2xl font-semibold mt-6")

    response = requests.get(f"{API_BASE}/drivers")
    if response.status_code == 200:
        drivers = response.json()  # Suppose it returns a list of drivers
    else:
        ui.label(f"Error fetching drivers: {response.text}")
        return
    
    with ui.column().classes("mt-4"):
        for d in drivers:
            with ui.row():
                driver_name = d.name
                driver_id = d.id
                page_link = ui.link(text=driver_name, target=ui.navigate.to(f"/driver/{driver_id}"), new_tab=True)
                
