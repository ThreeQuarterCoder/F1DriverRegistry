# delete_team.py
from nicegui import ui
from app.views.config import API_BASE
import requests

def delete_team_page():
    ui.label("Delete a Team").classes("text-2xl font-semibold mt-6")

    with ui.card().classes("w-1/2 mt-4"):
        team_id_input = ui.input("Team ID (e.g., teams/ABC123)")

        def do_delete():
            t_id = team_id_input.value.strip()
            if not t_id:
                ui.notify("Please enter a team ID.")
                return

            if "/" in t_id:
                t_id = t_id.split("/")[-1]

            resp = requests.delete(f"{API_BASE}/teams/{t_id}")
            if resp.status_code in (200, 204):
                ui.notify("Team deleted successfully!")
            else:
                ui.notify(f"Error deleting team: {resp.text}", close_button="OK")

        ui.button("Delete Team", on_click=do_delete).classes("bg-red-500 text-white mt-2")
