import fireo
import os 
from driver import Driver
from team import Team
from fireo.fields import TextField, NumberField, ReferenceField


# Initialize Fireo connection
fireo.connection(from_file="f1-driver-registry-b91545d3ebfc.json")

# --------------------------
# Step 1: CREATE TEAM & DRIVERS
# --------------------------
print("\n Creating a Team...")

# Create a team
team = Team(
    name="Red Bull Racing",
    year_founded=2005,
    total_pole_positions=98,
    total_race_wins=114,
    total_constructor_titles=6,
    finishing_position_previous_season=1
)
team.save()
print(f"Team Created: {team.id}, Name: {team.name}")

# Create three drivers for the team
drivers = [
    Driver(
        name="Max Verstappen",
        age=26,
        total_pole_positions=36,
        total_race_wins=56,
        total_points_scored=2500,
        total_world_titles=3,
        total_fastest_laps=28,
        team=team  # ReferenceField linking to Team
    ),
    Driver(
        name="Sergio Perez",
        age=34,
        total_pole_positions=2,
        total_race_wins=6,
        total_points_scored=1400,
        total_world_titles=0,
        total_fastest_laps=8,
        team=team
    ),
    Driver(
        name="Daniel Ricciardo",
        age=34,
        total_pole_positions=3,
        total_race_wins=8,
        total_points_scored=1200,
        total_world_titles=0,
        total_fastest_laps=10,
        team=team
    )
]

# Save drivers
for driver in drivers:
    driver.save()
    print(f" Driver Created: {driver.id}, Name: {driver.name}")

# --------------------------
# Step 2: READ DATA
# --------------------------
print("\n📄 Fetching Data...")

# Fetch the team
fetched_team = Team.collection.get(team.id)
print(f"Team Retrieved: {fetched_team.name}, Titles: {fetched_team.total_constructor_titles}")

# Fetch all drivers from Firestore linked to the team
print("\n Drivers in the Team:")
all_drivers = Driver.collection.filter("team", "==", team.key).fetch()
for d in all_drivers:
    print(f" - {d.name}, Wins: {d.total_race_wins}")

# --------------------------
# Step 3: UPDATE DATA
# --------------------------
print("\n🛠 Updating Data...")

# Update Max Verstappen's race wins
max_driver = Driver.collection.filter("name", "==", "Max Verstappen").filter("team", "==", team.key).get()
if max_driver:
    max_driver.total_race_wins += 1  # Increment by 1
    max_driver.update()
    print(f" Updated {max_driver.name}'s Wins to {max_driver.total_race_wins}")

# --------------------------
# Step 4: DELETE OBJECTS
# --------------------------
print("\n🗑 Deleting Data...")

# Delete all drivers
for d in all_drivers:
    Driver.collection.delete(d)
    print(f"🗑 Deleted Driver: {d.name}")
Driver.collection.delete_every()

# Delete the team
Team.collection.delete_every()
print(f"🗑 Deleted Team: {team.name}")

print("\n Fireo CRUD Operations Completed Successfully!")
