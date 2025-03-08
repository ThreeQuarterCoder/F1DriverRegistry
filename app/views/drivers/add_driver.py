# add_driver.py
from nicegui import ui
from app.views.config import API_BASE
import requests

def add_driver_page():
    ui.label("Add a New Driver").classes("text-2xl font-semibold mt-6")

    with ui.card().classes("w-1/2 mt-4"):
        ui.label("Enter driver details:").classes("text-lg")

        name_input = ui.input("Name")
        age_input = ui.number("Age")
        poles_input = ui.number("Total Pole Positions")
        wins_input = ui.number("Total Race Wins")
        points_input = ui.number("Total Points Scored")
        titles_input = ui.number("Total World Titles")
        fastest_laps_input = ui.number("Total Fastest Laps")
        team_input = ui.input("Team Reference (teams/XXX)")

        def create_driver():
            data = {
                "name": name_input.value,
                "age": age_input.value,
                "total_pole_positions": poles_input.value,
                "total_race_wins": wins_input.value,
                "total_points_scored": points_input.value,
                "total_world_titles": titles_input.value,
                "total_fastest_laps": fastest_laps_input.value,
                "team": team_input.value
            }

            resp = requests.post(f"{API_BASE}/drivers", json=data)
            if resp.status_code in (200, 201):
                ui.notify(f"Driver created successfully: {resp.json().get('name')}")
            else:
                ui.notify(f"Error creating driver: {resp.text}", close_button="OK")

        ui.button("Add Driver", on_click=create_driver).classes("bg-blue-500 text-white mt-2")
