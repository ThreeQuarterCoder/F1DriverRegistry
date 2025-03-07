from nicegui import ui 
from app.views.home import home_page

def register_view_routes():
    """Register View Routes"""
    ui.page("/") (home_page)
