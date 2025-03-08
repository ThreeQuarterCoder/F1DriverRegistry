from nicegui import ui
from app.views.config import API_BASE
import requests

def compare_teams_page():
    ui.label("Compare Two Teams").classes("text-2xl font-semibold mt-6")

    # Put the input fields in a card
    with ui.card().classes("w-1/2 mt-4"):
        ui.label("Enter two team IDs to compare:").classes("text-lg")

        team1_input = ui.input("Team 1 ID")
        team2_input = ui.input("Team 2 ID")

        results_container = ui.column().classes("mt-4")

        def do_compare():
            results_container.clear()
            t1_id = team1_input.value.strip()
            t2_id = team2_input.value.strip()
            if not t1_id or not t2_id:
                ui.label("Please enter both team IDs").parent(results_container)
                return

            # Call: GET /teams/compare?team1_id=...&team2_id=...
            params = {"team1_id": t1_id, "team2_id": t2_id}
            resp = requests.get(f"{API_BASE}/teams/compare", params=params)
            if resp.status_code == 200:
                data = resp.json()
                if "comparison" not in data:
                    ui.label("Unexpected response format.").parent(results_container)
                    return
                # data has e.g. data["team1"], data["team2"], data["comparison"][]

                # Display team names
                team1_name = data["team1"].get("name", "Team1")
                team2_name = data["team2"].get("name", "Team2")

                ui.label(f"Comparing: {team1_name} vs. {team2_name}").classes("text-xl").parent(results_container)

                # Build a two-column table
                with results_container.row() as table_row:
                    # Table header
                    ui.label("").classes("w-32")  # left column for field name
                    ui.label(team1_name).classes("w-32 font-semibold text-center")
                    ui.label(team2_name).classes("w-32 font-semibold text-center")

                comparison_list = data["comparison"]  # array of objects
                for row in comparison_list:
                    field = row["field"]
                    val1 = row["team1_value"]
                    val2 = row["team2_value"]
                    better = row["better"]  # "team1", "team2", or "equal"

                    with results_container.row() as table_row:
                        ui.label(field).classes("w-32 font-semibold")
                        
                        # This is Team1's cell
                        cell1 = ui.label(f"{val1}").classes("w-32 text-center")
                        # This is Team2's cell
                        cell2 = ui.label(f"{val2}").classes("w-32 text-center")

                        # Highlight the better cell
                        if better == "team1":
                            cell1.classes("bg-green-200")
                        elif better == "team2":
                            cell2.classes("bg-green-200")
                        # if "equal", no highlight
            else:
                ui.label(f"Error: {resp.text}").classes("text-red-500").parent(results_container)

        ui.button("Compare", on_click=do_compare).classes("bg-blue-500 text-white mt-2")
