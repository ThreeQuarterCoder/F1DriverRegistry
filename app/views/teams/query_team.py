from nicegui import ui
from app.views.config import API_BASE
import requests

def team_query_page():
    ui.label("Query Teams").classes("text-2xl font-semibold mt-6")

    # We'll store the search form in a card
    with ui.card().classes("w-1/2 mt-4"):
        ui.label("Enter your query parameters:").classes("text-lg")

        # Example attribute dropdown
        attribute_input = ui.select(
            options=["year_founded", "total_pole_positions", "total_race_wins", "total_constructor_titles", "finishing_position_previous_season"],
            value="year_founded",
            label="Attribute"
        )

        # Operator dropdown
        operator_input = ui.select(
            options=["<", ">", "="],
            value=">",
            label="Operator"
        )

        # Numeric value input
        value_input = ui.number(label="Value", value=1950)

        # We'll create a button to trigger the search
        def on_search():
            attribute = attribute_input.value
            operator = operator_input.value
            v = value_input.value

            # Call GET /teams/query?attribute=...&operator=...&value=...
            params = {"attribute": attribute, "operator": operator, "value": v}
            resp = requests.get(f"{API_BASE}/teams/query", params=params)

            # Clear previous results
            results_column.clear()

            if resp.status_code == 200:
                teams = resp.json()  # should be a list of dicts
                if not teams:
                    ui.label("No matching teams found.").classes("text-gray-500").parent(results_column)
                    return

                for t in teams:
                    # e.g.  t = { "id": "teams/<docId>", "name": "...", etc. }
                    team_name = t.get("name")
                    team_id = t.get("id")
                    with results_column.row():
                        ui.link(
                            text=f"{team_name}",
                            target=f"/team/{team_id}"
                        )
            else:
                ui.label(f"Error: {resp.text}").classes("text-red-500").parent(results_column)

        ui.button("Search", on_click=on_search).classes("bg-blue-500 text-white mt-2")

    # We'll display results in a separate column, so we can clear/refresh easily
    results_column = ui.column().classes("mt-4")
