from nicegui import ui
from app.views.config import API_BASE
import requests

def driver_query_page():
    ui.label("Query Drivers").classes("text-2xl font-semibold mt-6")

    # A card for the query form
    with ui.card().classes("w-1/2 mt-4"):
        ui.label("Enter your driver filter criteria:").classes("text-lg")

        # 1) Driver attribute
        attribute_input = ui.select(
            options=[
                "age",
                "total_pole_positions",
                "total_race_wins",
                "total_points_scored",
                "total_world_titles",
                "total_fastest_laps"
            ],
            value="age",
            label="Attribute"
        )

        # 2) Operator (<, >, =)
        operator_input = ui.select(
            options=["<", ">", "="],
            value=">",
            label="Operator"
        )

        # 3) Numeric value
        value_input = ui.number(label="Value", value=30)

        # 4) Container for the resulting driver list
        results_column = ui.column().classes("mt-4")

        # Function to call the /drivers/query endpoint
        def on_search():
            # Clear any existing results
            results_column.clear()

            attribute = attribute_input.value
            operator = operator_input.value
            numeric_val = value_input.value

            params = {
                "attribute": attribute,
                "operator": operator,
                "value": numeric_val
            }

            resp = requests.get(f"{API_BASE}/drivers/query", params=params)
            if resp.status_code == 200:
                drivers = resp.json()  # list of dicts from your driver.to_dict()
                if not drivers:
                    ui.label("No matching drivers found.").parent(results_column)
                    return

                for d in drivers:
                    driver_name = d.get("name", "Unknown")
                    driver_id   = d.get("id")  # from driver.to_dict() if data["id"] = self.key
                    team_name   = d.get("team_name", None)  # only if you embed this in to_dict()
                    team_id     = d.get("team_id", None)

                    with results_column.row():
                        # Link to driver detail page
                        ui.link(
                            text=driver_name,
                            target=f"/driver/{driver_id}"
                        )
                        # If the driver has a team, show a link to that team as well
                        if team_id:
                            ui.label(" | ")  # separator
                            ui.link(
                                text=f"Team: {team_name}",
                                target=f"/team/{team_id}"
                            )
            else:
                ui.label(f"Error: {resp.text}").classes("text-red-500").parent(results_column)

        # 5) Search button
        ui.button("Search", on_click=on_search).classes("bg-blue-500 text-white mt-2")
