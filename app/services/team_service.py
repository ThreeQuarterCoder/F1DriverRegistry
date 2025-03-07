# team_service.py

from typing import List
from app.models.team import Team

class TeamService:
    @staticmethod
    def create_team(data: dict) -> Team:
        team = Team(**data).save()
        return team

    @staticmethod
    def get_team(team_id: str) -> Team:
        return Team.collection.get(team_id)

    @staticmethod
    def update_team(team_id: str, data: dict) -> Team:
        team = TeamService.get_team(team_id)
        for key, value in data.items():
            setattr(team, key, value)
        team.save()
        return team

    @staticmethod
    def delete_team(team_id: str) -> None:
        team = TeamService.get_team(team_id)
        if team:
            team.delete()

    @staticmethod
    def list_teams() -> List[Team]:
        return Team.collection.fetch()

    @staticmethod
    def filter_teams(attribute: str, operator: str, value: float) -> List[Team]:
        filter_str = f"{attribute}{operator}"
        return Team.collection.filter(filter_str, value).fetch()

    @staticmethod
    def compare_teams(t1_id: str, t2_id: str) -> dict:
        t1 = TeamService.get_team(t1_id)
        t2 = TeamService.get_team(t2_id)
        if not t1 or not t2:
            return {"error": "One or both teams not found"}

        # Compare key fields
        fields_to_compare = [
            "year_founded",
            "total_pole_positions",
            "total_race_wins",
            "total_constructor_titles",
            "finishing_position_previous_season"
        ]

        comparison_results = []
        for field in fields_to_compare:
            val1 = getattr(t1, field, 0) or 0
            val2 = getattr(t2, field, 0) or 0

            # Some fields might treat lower as better (finishing_position_previous_season, year_founded?), 
            # define logic as needed:
            if field in ["year_founded", "finishing_position_previous_season"]:
                # lower is better
                if val1 < val2:
                    better = "team1"
                elif val2 < val1:
                    better = "team2"
                else:
                    better = "equal"
            else:
                # higher is better
                if val1 > val2:
                    better = "team1"
                elif val2 > val1:
                    better = "team2"
                else:
                    better = "equal"

            comparison_results.append({
                "field": field,
                "team1_value": val1,
                "team2_value": val2,
                "better": better
            })

        return {
            "team1": t1.to_dict(),
            "team2": t2.to_dict(),
            "comparison": comparison_results
        }