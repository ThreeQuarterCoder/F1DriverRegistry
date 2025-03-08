# modify_driver.py
from nicegui import ui
from app.views.config import API_BASE
import requests

def modify_driver_page():
    ui.label("Modify an Existing Driver").classes("text-2xl font-semibold mt-6")

    with ui.card().classes("w-1/2 mt-4"):
        ui.label("Enter driver ID and new attributes:").classes("text-lg")

        driver_id_input = ui.input("Driver ID (e.g., drivers/ABC123)")

        name_input = ui.input("Name (leave blank to keep unchanged)")
        age_input = ui.number("Age (0 = no change)", value=0)
        poles_input = ui.number("Total Pole Positions (0 = no change)", value=0)
        wins_input = ui.number("Total Race Wins (0 = no change)", value=0)
        points_input = ui.number("Total Points (0 = no change)", value=0)
        titles_input = ui.number("World Titles (0 = no change)", value=0)
        laps_input = ui.number("Fastest Laps (0 = no change)", value=0)
        team_input = ui.input("Team Reference (leave blank to keep)")

        def update_driver():
            drv_id = driver_id_input.value.strip()
            if not drv_id:
                ui.notify("Please enter a driver ID.")
                return

            # Build data only for changed fields
            data = {}
            if name_input.value:
                data["name"] = name_input.value
            if age_input.value:
                data["age"] = age_input.value
            if poles_input.value:
                data["total_pole_positions"] = poles_input.value
            if wins_input.value:
                data["total_race_wins"] = wins_input.value
            if points_input.value:
                data["total_points_scored"] = points_input.value
            if titles_input.value:
                data["total_world_titles"] = titles_input.value
            if laps_input.value:
                data["total_fastest_laps"] = laps_input.value
            if team_input.value:
                data["team"] = team_input.value

            # For example: PUT /drivers/{driver_id_input}
            # If driver_id_input includes "drivers/ABC123", we might do a substring. 
            # Or your backend might accept the full doc path. Adjust as needed.
            if "/" in drv_id:
                # If user typed "drivers/ABC123", split
                drv_id = drv_id.split('/')[-1]

            resp = requests.put(f"{API_BASE}/drivers/{drv_id}", json=data)
            if resp.status_code == 200:
                ui.notify(f"Driver updated: {resp.json().get('name')}")
            else:
                ui.notify(f"Error updating driver: {resp.text}", close_button="OK")

        ui.button("Update Driver", on_click=update_driver).classes("bg-blue-500 text-white mt-2")
