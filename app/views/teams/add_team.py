# add_team.py
from nicegui import ui
from app.views.config import API_BASE
import requests

def add_team_page():
    ui.label("Add a New Team").classes("text-2xl font-semibold mt-6")

    with ui.card().classes("w-1/2 mt-4"):
        ui.label("Enter team details:").classes("text-lg")

        name_input = ui.input("Team Name")
        founded_input = ui.number("Year Founded")
        poles_input = ui.number("Total Pole Positions")
        wins_input = ui.number("Total Race Wins")
        titles_input = ui.number("Total Constructor Titles")
        finishing_input = ui.number("Finishing Position Previous Season")

        def create_team():
            data = {
                "name": name_input.value,
                "year_founded": founded_input.value,
                "total_pole_positions": poles_input.value,
                "total_race_wins": wins_input.value,
                "total_constructor_titles": titles_input.value,
                "finishing_position_previous_season": finishing_input.value
            }
            resp = requests.post(f"{API_BASE}/teams", json=data)
            if resp.status_code in (200, 201):
                ui.notify(f"Team created: {resp.json().get('name')}")
            else:
                ui.notify(f"Error creating team: {resp.text}", close_button="OK")

        ui.button("Add Team", on_click=create_team).classes("bg-green-500 text-white mt-2")
