"""
Content Agency Creative Capacity & Sprint Velocity Planner
Calculates team utilization and capacity bottlenecks for marketing creative production:
- Resource hours by skill role (Motion Designer, Video Editor, Copywriter, Graphic Designer)
- Standardized asset effort benchmarks (e.g., Short Video = 4.5h, Carousel = 2.5h, Static = 1.0h)
- Team utilization percentage & maximum deliverable throughput
"""
import json
import argparse
from typing import List, Dict, Any

EFFORT_BENCHMARKS = {
    "short_video_reel": {"video_editor": 3.5, "copywriter": 1.0},
    "motion_ad_complex": {"motion_designer": 6.0, "copywriter": 1.5},
    "carousel_10_slides": {"graphic_designer": 2.5, "copywriter": 1.0},
    "static_banner_ad": {"graphic_designer": 1.0, "copywriter": 0.5}
}

def calculate_agency_capacity(team_roster: List[Dict[str, Any]], deliverable_queue: List[Dict[str, Any]]) -> Dict[str, Any]:
    available_hours = {}
    for member in team_roster:
        role = member["role"]
        hours = member.get("weekly_hours", 40) * 0.80  # 80% billable utilization target
        available_hours[role] = available_hours.get(role, 0.0) + hours
        
    required_hours = {}
    for item in deliverable_queue:
        asset_type = item.get("asset_type")
        qty = item.get("quantity", 1)
        effort = EFFORT_BENCHMARKS.get(asset_type, {"graphic_designer": 1.5, "copywriter": 1.0})
        
        for role, hrs in effort.items():
            required_hours[role] = required_hours.get(role, 0.0) + (hrs * qty)
            
    utilization_by_role = {}
    bottlenecks = []
    
    all_roles = set(available_hours.keys()).union(set(required_hours.keys()))
    for r in all_roles:
        avail = available_hours.get(r, 0.0)
        req = required_hours.get(r, 0.0)
        util = round((req / avail * 100.0), 1) if avail > 0 else 999.0
        utilization_by_role[r] = {
            "available_hours": avail,
            "required_hours": req,
            "utilization_pct": util
        }
        if util > 100.0:
            bottlenecks.append(f"{r} over capacity at {util}%")
            
    return {
        "team_size": len(team_roster),
        "total_deliverables_queued": sum(i.get("quantity", 1) for i in deliverable_queue),
        "utilization_by_role": utilization_by_role,
        "bottlenecks": bottlenecks,
        "is_sprint_achievable": len(bottlenecks) == 0
    }

def main():
    team = [
        {"name": "Sara", "role": "copywriter", "weekly_hours": 40},
        {"name": "Omar", "role": "graphic_designer", "weekly_hours": 40},
        {"name": "Karim", "role": "video_editor", "weekly_hours": 40}
    ]
    queue = [
        {"asset_type": "short_video_reel", "quantity": 6},
        {"asset_type": "carousel_10_slides", "quantity": 8}
    ]
    res = calculate_agency_capacity(team, queue)
    print(json.dumps(res, indent=2))

if __name__ == "__main__":
    main()
