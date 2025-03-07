# driver_controller.py
from fastapi import APIRouter, HTTPException, Depends, Query
from typing import Any, List, Optional
from services.driver_service import DriverService

driver_router = APIRouter(prefix="/drivers", tags=["drivers"])

# For authentication, you might do something like:
# from auth import auth_required
# and then add 'current_user = Depends(auth_required)' to restricted routes.

@driver_router.get("", response_model=List[Any])
def list_drivers():
    drivers = DriverService.list_drivers()
    return [d.to_dict() for d in drivers]

@driver_router.get("/{driver_id}", response_model=dict)
def get_driver(driver_id: str):
    driver = DriverService.get_driver(driver_id)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver.to_dict()

@driver_router.post("", response_model=dict)
def create_driver(data: dict):  # , current_user=Depends(auth_required)
    new_driver = DriverService.create_driver(data)
    return new_driver.to_dict()

@driver_router.put("/{driver_id}", response_model=dict)
def update_driver(driver_id: str, data: dict):  # , current_user=Depends(auth_required)
    updated = DriverService.update_driver(driver_id, data)
    if not updated:
        raise HTTPException(status_code=404, detail="Driver not found")
    return updated.to_dict()

@driver_router.delete("/{driver_id}")
def delete_driver(driver_id: str):  # , current_user=Depends(auth_required)
    success = DriverService.delete_driver(driver_id)
    if not success:
        raise HTTPException(status_code=404, detail="Driver not found")
    return {"message": "Driver deleted successfully"}

@driver_router.get("/query", response_model=List[Any])
def query_drivers(
    attribute: str,
    operator: str = Query(..., regex="^(<|>|=)$"),
    value: float = 0
):
    """
    Example: GET /drivers/query?attribute=age&operator=>&value=30
    """
    drivers = DriverService.filter_drivers(attribute, operator, value)
    return [d.to_dict() for d in drivers]

@driver_router.get("/compare")
def compare_drivers(driver1_id: str, driver2_id: str):
    comparison = DriverService.compare_drivers(driver1_id, driver2_id)
    return comparison
