# team_controller.py
from fastapi import APIRouter, HTTPException, Depends, Query
from typing import Any, List
from services.team_service import TeamService

team_router = APIRouter(prefix="/teams", tags=["teams"])

@team_router.get("", response_model=List[Any])
def list_teams():
    teams = TeamService.list_teams()
    return [t.to_dict() for t in teams]

@team_router.get("/{team_id}", response_model=dict)
def get_team(team_id: str):
    team = TeamService.get_team(team_id)
    if not team:
        raise HTTPException(status_code=404, detail="Team not found")
    return team.to_dict()

@team_router.post("", response_model=dict)
def create_team(data: dict):  # , current_user=Depends(auth_required)
    new_team = TeamService.create_team(data)
    return new_team.to_dict()

@team_router.put("/{team_id}", response_model=dict)
def update_team(team_id: str, data: dict):  # , current_user=Depends(auth_required)
    updated = TeamService.update_team(team_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Team not found")
    return updated.to_dict()

@team_router.delete("/{team_id}")
def delete_team(team_id: str):  # , current_user=Depends(auth_required)
    success = TeamService.delete_team(team_id)
    if not success:
        raise HTTPException(status_code=404, detail="Team not found")
    return {"message": "Team deleted successfully"}

@team_router.get("/query", response_model=List[Any])
def query_teams(
    attribute: str,
    operator: str = Query(..., regex="^(<|>|=)$"),
    value: float = 0
):
    teams = TeamService.filter_teams(attribute, operator, value)
    return [t.to_dict() for t in teams]

@team_router.get("/compare")
def compare_teams(team1_id: str, team2_id: str):
    comparison = TeamService.compare_teams(team1_id, team2_id)
    return comparison
