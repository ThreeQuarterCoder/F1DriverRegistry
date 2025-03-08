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

    def to_dict(self):
        base = super()._data  # or something like self._data

        data = {
            "name": self.name,
            "year_founded": self.year_founded,
            "total_pole_positions": self.total_pole_positions,
            "total_race_wins": self.total_race_wins,
            "total_constructor_titles": self.total_constructor_titles,
            "finishing_position_previous_season": self.finishing_position_previous_season
        }
        
        data["id"] = self.key  
        return data