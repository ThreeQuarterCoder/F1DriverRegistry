import fireo
from fireo.models import Model
from fireo.fields import TextField, NumberField, ReferenceField
from team import Team

class Driver(Model):
    name = TextField()
    age = NumberField()
    total_pole_positions = NumberField()
    total_race_wins = NumberField() 
    total_points_scored = NumberField()
    total_world_titles = NumberField()
    total_fastest_laps = NumberField()
    team = ReferenceField(Team)
