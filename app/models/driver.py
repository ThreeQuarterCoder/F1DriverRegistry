import fireo
from fireo.models import Model
from fireo.fields import TextField, NumberField, ReferenceField
from app.models.team import Team

class Driver(Model):
    name = TextField()
    age = NumberField()
    total_pole_positions = NumberField()
    total_race_wins = NumberField() 
    total_points_scored = NumberField()
    total_world_titles = NumberField()
    total_fastest_laps = NumberField()
    team = ReferenceField(Team)

    def to_dict(self):
        base = super()._data  # or something like self._data

        data = {
            "name": self.name,
            "age": self.age,
            "total_pole_positions": self.total_pole_positions,
            "total_race_wins": self.total_race_wins,
            "total_points_scored": self.total_points_scored,
            "total_world_titles": self.total_world_titles,
            "total_fastest_laps": self.total_fastest_laps,
            "team": self.team
        }
        
        data["id"] = self.key  
        return data
