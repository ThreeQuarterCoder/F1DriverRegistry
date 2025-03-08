from nicegui import ui

from app.controllers.view_controller import register_view_routes

ui.add_static_files('/static', os.path.join(os.path.dirname(__file__), 'static'))

register_view_routes()

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title="F1 Registry", host="127.0.0.1", port=8001)