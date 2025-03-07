# driver_service.py

from typing import List
from app.models.driver import Driver  # your FireO driver model

class DriverService:
    @staticmethod
    def create_driver(data: dict) -> Driver:
        # data contains name, age, total_race_wins, etc.
        driver = Driver(**data).save()
        return driver

    @staticmethod
    def get_driver(driver_id: str) -> Driver:
        return Driver.collection.get(driver_id)

    @staticmethod
    def update_driver(driver_id: str, data: dict) -> Driver:
        driver = DriverService.get_driver(driver_id)
        for key, value in data.items():
            setattr(driver, key, value)
        driver.save()
        return driver

    @staticmethod
    def delete_driver(driver_id: str) -> None:
        driver = DriverService.get_driver(driver_id)
        if driver:
            driver.delete()

    @staticmethod
    def list_drivers() -> List[Driver]:
        return Driver.collection.fetch()

    @staticmethod
    def filter_drivers(attribute: str, operator: str, value: float) -> List[Driver]:
        """
        For example, if operator='>' then do .filter("age>", 30)
        """
        filter_str = f"{attribute}{operator}"
        return Driver.collection.filter(filter_str, value).fetch()

    @staticmethod
    def compare_drivers(d1_id: str, d2_id: str) -> dict:
        d1 = DriverService.get_driver(d1_id)
        d2 = DriverService.get_driver(d2_id)
        if not d1 or not d2:
            return {"error": "One or both drivers not found"}

        # For simplicity, compare a subset of relevant fields:
        fields_to_compare = [
            "age",
            "total_pole_positions",
            "total_race_wins",
            "total_points_scored",
            "total_world_titles",
            "total_fastest_laps"
        ]

        comparison_results = []
        for field in fields_to_compare:
            val1 = getattr(d1, field, 0) or 0
            val2 = getattr(d2, field, 0) or 0

            # "Better" means higher value, for example:
            # you can add special logic for certain fields
            if val1 > val2:
                better = "driver1"
            elif val2 > val1:
                better = "driver2"
            else:
                better = "equal"

            comparison_results.append({
                "field": field,
                "driver1_value": val1,
                "driver2_value": val2,
                "better": better
            })

        return {
            "driver1": d1.to_dict(),
            "driver2": d2.to_dict(),
            "comparison": comparison_results
        }
