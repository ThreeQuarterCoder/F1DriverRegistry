# delete_driver.py
from nicegui import ui
from app.views.config import API_BASE
import requests

def delete_driver_page():
    ui.label("Delete a Driver").classes("text-2xl font-semibold mt-6")

    with ui.card().classes("w-1/2 mt-4"):
        driver_id_input = ui.input("Driver ID (e.g., drivers/ABC123)")
        
        def do_delete():
            drv_id = driver_id_input.value.strip()
            if not drv_id:
                ui.notify("Please enter driver ID.")
                return

            if "/" in drv_id:
                drv_id = drv_id.split("/")[-1]

            resp = requests.delete(f"{API_BASE}/drivers/{drv_id}")
            if resp.status_code in (200, 204):
                ui.notify("Driver deleted successfully!")
            else:
                ui.notify(f"Error deleting driver: {resp.text}", close_button="OK")

        ui.button("Delete Driver", on_click=do_delete).classes("bg-red-500 text-white mt-2")
