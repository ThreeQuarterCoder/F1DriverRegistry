from nicegui import ui

def home_page():
    ui.label("Welcome to F1 Driver Registry").classes("text-3xl font-bold mt-6")

    with ui.row().classes("mt-4"):
        ui.button("Manage Drivers", on_click=lambda: ui.navigate("/drivers")).classes("bg-blue-500 text-white p-2 rounded")
        ui.button("Manage Teams", on_click=lambda: ui.navigate("/teams")).classes("bg-green-500 text-white p-2 rounded")