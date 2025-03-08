from nicegui import ui
from app.views.config import API_BASE
import requests

def compare_drivers_page():
    ui.label("Compare Two Drivers").classes("text-2xl font-semibold mt-6")

    with ui.card().classes("w-1/2 mt-4"):
        ui.label("Enter two driver IDs to compare:").classes("text-lg")

        driver1_input = ui.input("Driver 1 ID")
        driver2_input = ui.input("Driver 2 ID")

        results_container = ui.column().classes("mt-4")

        def do_compare():
            results_container.clear()
            d1_id = driver1_input.value.strip()
            d2_id = driver2_input.value.strip()
            if not d1_id or not d2_id:
                ui.label("Please enter both driver IDs").parent(results_container)
                return

            # GET /drivers/compare?driver1_id=...&driver2_id=...
            params = {"driver1_id": d1_id, "driver2_id": d2_id}
            resp = requests.get(f"{API_BASE}/drivers/compare", params=params)
            if resp.status_code == 200:
                data = resp.json()
                if "comparison" not in data:
                    ui.label("Unexpected response format.").parent(results_container)
                    return
                driver1_name = data["driver1"].get("name", "Driver1")
                driver2_name = data["driver2"].get("name", "Driver2")

                ui.label(f"Comparing: {driver1_name} vs. {driver2_name}").classes("text-xl").parent(results_container)

                with results_container.row():
                    ui.label("").classes("w-32")
                    ui.label(driver1_name).classes("w-32 font-semibold text-center")
                    ui.label(driver2_name).classes("w-32 font-semibold text-center")

                for row in data["comparison"]:
                    field = row["field"]
                    val1 = row["driver1_value"]
                    val2 = row["driver2_value"]
                    better = row["better"]  # "driver1", "driver2", or "equal"

                    with results_container.row():
                        ui.label(field).classes("w-32 font-semibold")

                        cell1 = ui.label(str(val1)).classes("w-32 text-center")
                        cell2 = ui.label(str(val2)).classes("w-32 text-center")

                        if better == "driver1":
                            cell1.classes("bg-green-200")
                        elif better == "driver2":
                            cell2.classes("bg-green-200")
            else:
                ui.label(f"Error: {resp.text}").classes("text-red-500").parent(results_container)

        ui.button("Compare", on_click=do_compare).classes("bg-blue-500 text-white mt-2")
