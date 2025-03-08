from nicegui import ui
from app.views.config import API_BASE

def home_page():

    with ui.card().classes("w-1/2 mt-4"):
        # We'll put placeholders (labels, buttons) inside that we can show/hide via JS
        with ui.row().props("id=loggedOutPanel"):
            ui.label("You are currently logged out.").classes("text-gray-500")
            ui.button("Log In", on_click=lambda: ui.run_javascript("showLoginDialog()"))

        with ui.row().props("id=loggedInPanel style=display:none"):
            ui.label("Logged in as: ").props("id=userEmailLabel")
            ui.button("Log Out", on_click=lambda: ui.run_javascript("signOutUser()"))

    with ui.row().classes("mt-4"):
        ui.button("View Drivers", on_click=lambda: ui.navigate.to("/drivers")).classes("bg-blue-500 text-white p-2 rounded")
        ui.button("View Teams", on_click=lambda: ui.navigate.to("/teams")).classes("bg-blue-500 text-white p-2 rounded")
        ui.button("Compare Teams", on_click=lambda: ui.navigate.to("/team/compare")).classes("bg-blue-500 text-white p-2 rounded")
        ui.button("Compare Drivers", on_click=lambda: ui.navigate.to("/driver/compare")).classes("bg-blue-500 text-white p-2 rounded")
        ui.button("Query Teams", on_click=lambda: ui.navigate.to("/team/query")).classes("bg-blue-500 text-white p-2 rounded")
        ui.button("Query Drivers", on_click=lambda: ui.navigate.to("/driver/query")).classes("bg-blue-500 text-white p-2 rounded")
        # ui.button("Add Driver", on_click=lambda: ui.navigate.to("/driver/add")).classes("bg-blue-500 text-white p-2 rounded")
        # ui.button("Modify Driver", on_click=lambda: ui.navigate.to("/driver/modify")).classes("bg-blue-500 text-white p-2 rounded")
        # ui.button("Delete Driver", on_click=lambda: ui.navigate.to("/driver/delete")).classes("bg-blue-500 text-white p-2 rounded")
        # ui.button("Add Team", on_click=lambda: ui.navigate.to("/team/add")).classes("bg-blue-500 text-white p-2 rounded")
        # ui.button("Modify Team", on_click=lambda: ui.navigate.to("/team/modify")).classes("bg-blue-500 text-white p-2 rounded")
        # ui.button("Delete Team", on_click=lambda: ui.navigate.to("/team/delete")).classes("bg-blue-500 text-white p-2 rounded")
        ui.button("Add Driver", on_click=lambda: ui.navigate.to("/driver/add")) \
            .props("id=btn_add_driver style=display:none") \
            .classes("bg-blue-500 text-white p-2 rounded")

        ui.button("Modify Driver", on_click=lambda: ui.navigate.to("/driver/modify")) \
            .props("id=btn_modify_driver style=display:none") \
            .classes("bg-blue-500 text-white p-2 rounded")

        ui.button("Delete Driver", on_click=lambda: ui.navigate.to("/driver/delete")) \
            .props("id=btn_delete_driver style=display:none") \
            .classes("bg-blue-500 text-white p-2 rounded")

        ui.button("Add Team", on_click=lambda: ui.navigate.to("/team/add")) \
            .props("id=btn_add_team style=display:none") \
            .classes("bg-blue-500 text-white p-2 rounded")

        ui.button("Modify Team", on_click=lambda: ui.navigate.to("/team/modify")) \
            .props("id=btn_modify_team style=display:none") \
            .classes("bg-blue-500 text-white p-2 rounded")

        ui.button("Delete Team", on_click=lambda: ui.navigate.to("/team/delete")) \
            .props("id=btn_delete_team style=display:none") \
            .classes("bg-blue-500 text-white p-2 rounded")
