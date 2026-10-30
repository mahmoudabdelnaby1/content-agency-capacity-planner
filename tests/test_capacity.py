"""
Unit tests for Agency Capacity Planner
"""
import unittest
from src.calc_capacity import calculate_agency_capacity

class TestAgencyCapacity(unittest.TestCase):
    def test_capacity_within_limits(self):
        team = [
            {"name": "Sara", "role": "copywriter", "weekly_hours": 40},
            {"name": "Omar", "role": "graphic_designer", "weekly_hours": 40}
        ]
        queue = [{"asset_type": "static_banner_ad", "quantity": 10}]
        res = calculate_agency_capacity(team, queue)
        self.assertTrue(res["is_sprint_achievable"])
        self.assertLess(res["utilization_by_role"]["copywriter"]["utilization_pct"], 100.0)

if __name__ == "__main__":
    unittest.main()
