# modify_team.py
from nicegui import ui
from app.views.config import API_BASE
import requests

def modify_team_page():
    ui.label("Modify an Existing Team").classes("text-2xl font-semibold mt-6")

    with ui.card().classes("w-1/2 mt-4"):
        ui.label("Enter team ID and new attributes:").classes("text-lg")

        team_id_input = ui.input("Team ID (e.g., teams/ABC123)")

        name_input = ui.input("New Team Name (leave blank to keep)")
        founded_input = ui.number("Year Founded (0=unchanged)", value=0)
        poles_input = ui.number("Total Pole Positions (0=unchanged)", value=0)
        wins_input = ui.number("Total Race Wins (0=unchanged)", value=0)
        titles_input = ui.number("Constructor Titles (0=unchanged)", value=0)
        finishing_input = ui.number("Finishing Pos Prev Season (0=unchanged)", value=0)

        def update_team():
            t_id = team_id_input.value.strip()
            if not t_id:
                ui.notify("Please enter a team ID.")
                return

            if "/" in t_id:
                t_id = t_id.split("/")[-1]

            data = {}
            if name_input.value:
                data["name"] = name_input.value
            if founded_input.value:
                data["year_founded"] = founded_input.value
            if poles_input.value:
                data["total_pole_positions"] = poles_input.value
            if wins_input.value:
                data["total_race_wins"] = wins_input.value
            if titles_input.value:
                data["total_constructor_titles"] = titles_input.value
            if finishing_input.value:
                data["finishing_position_previous_season"] = finishing_input.value

            resp = requests.put(f"{API_BASE}/teams/{t_id}", json=data)
            if resp.status_code == 200:
                ui.notify(f"Team updated: {resp.json().get('name')}")
            else:
                ui.notify(f"Error updating team: {resp.text}", close_button="OK")

        ui.button("Update Team", on_click=update_team).classes("bg-green-500 text-white mt-2")
