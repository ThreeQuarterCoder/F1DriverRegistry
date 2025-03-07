import fireo
from fireo.models import Model
from fireo.fields import TextField, NumberField, ReferenceField

class Team(Model):
    name = TextField()
    year_founded = NumberField()
    total_pole_positions = NumberField()
    total_race_wins = NumberField()
    total_constructor_titles = NumberField()
    finishing_position_previous_season = NumberField()