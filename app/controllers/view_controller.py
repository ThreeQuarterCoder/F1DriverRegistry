from nicegui import ui 
from app.views.home import home_page
from app.views.drivers.add_driver import add_driver_page
from app.views.drivers.modify_driver import modify_driver_page
from app.views.drivers.delete_driver import delete_driver_page
from app.views.teams.add_team import add_team_page
from app.views.teams.modify_team import modify_team_page
from app.views.teams.delete_team import delete_team_page
from app.views.drivers.view_drivers import driver_list_page
from app.views.drivers.query_driver import driver_query_page
from app.views.drivers.view_driver import driver_detail_page
from app.views.drivers.compare_drivers import compare_drivers_page
from app.views.teams.view_teams import team_list_page
from app.views.teams.query_team import team_query_page
from app.views.teams.compare_teams import compare_teams_page
from app.views.teams.view_team import team_detail_page

def register_view_routes():

    ui.add_head_html("""
        <script type="module" src="/static/firebase-login.js"></script>
        """)
    ui.label("Welcome to F1 Driver Registry").classes("text-3xl font-bold mt-6")
    """Register View Routes"""
    ui.page("/") (home_page)
    # Drivers
    ui.page("/drivers")(driver_list_page)
    ui.page("/driver/{driver_id}")(driver_detail_page)
    ui.page("/driver/query")(driver_query_page)
    ui.page("/driver/add")(add_driver_page)
    ui.page("/driver/modify")(modify_driver_page)
    ui.page("/driver/delete")(delete_driver_page)

    # Teams
    ui.page("/teams")(team_list_page)
    ui.page("/team/{team_id}")(team_detail_page)
    ui.page("/team/query")(team_query_page)
    ui.page("/team/add")(add_team_page)
    ui.page("/team/modify")(modify_team_page)
    ui.page("/team/delete")(delete_team_page)

    # Compare
    ui.page("/driver/compare")(compare_drivers_page)
    ui.page("/team/compare")(compare_teams_page)
