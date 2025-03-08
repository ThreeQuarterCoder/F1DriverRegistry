from nicegui import ui
from app.views.config import API_BASE

def home_page():

    with ui.card().classes("w-1/2 mt-4"):
        # We'll put placeholders (labels, buttons) inside that we can show/hide via JS
        with ui.row().props("id=loggedOutPanel"):
            ui.label("You are currently logged out.").classes("text-gray-500")
            ui.button("Log In", on_click=lambda: ui.run_javascript("showLoginDialog()"))

        with ui.row().props("id=loggedInPanel", style="display:none"):
            ui.label("Logged in as: ").props("id=userEmailLabel")
            ui.button("Log Out", on_click=lambda: ui.run_javascript("signOutUser()"))

    with ui.row().classes("mt-4"):
        ui.button("View Drivers", on_click=lambda: ui.navigate.to("/drivers")).classes("bg-blue-500 text-white p-2 rounded")
        ui.button("View Teams", on_click=lambda: ui.navigate.to("/teams")).classes("bg-green-500 text-white p-2 rounded")