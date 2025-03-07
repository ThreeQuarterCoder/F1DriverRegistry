from nicegui import ui 
from app.views.home import home_page

def register_view_routes():
    """Register View Routes"""
    ui.page("/") (home_page)
    # Drivers
    ui.page("/drivers")(driver_list_page)
    ui.page("/driver/{driver_id}")(driver_detail_page)
    ui.page("/driver/query")(driver_search_page)

    # Teams
    ui.page("/teams")(team_list_page)
    ui.page("/team/{team_id}")(team_detail_page)
    ui.page("/team/query")(team_search_page)

    # Compare
    ui.page("/driver/compare")(compare_drivers_page)
    ui.page("/team/compare")(compare_teams_page)
