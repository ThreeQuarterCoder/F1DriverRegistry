from nicegui import ui

def home_page():
    ui.label("Welcome to F1 Driver Registry").classes("text-3xl font-bold mt-6")

    with ui.row().classes("mt-4"):
        ui.button("View Drivers", on_click=lambda: ui.navigate.to("/drivers")).classes("bg-blue-500 text-white p-2 rounded")
        ui.button("View Teams", on_click=lambda: ui.navigate.to("/teams")).classes("bg-green-500 text-white p-2 rounded")