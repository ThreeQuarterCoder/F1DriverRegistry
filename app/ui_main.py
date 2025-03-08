from nicegui import ui

from app.controllers.view_controller import register_view_routes

register_view_routes()

if __name__ == "__main__":
    ui.run(title="F1 Registry", host="127.0.0.1", port=8001)