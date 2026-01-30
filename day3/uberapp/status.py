
from __future__ import annotations

from typing import Dict

STATUS_FLOW = ("WAITING", "STARTED", "COMPLETED")

def update_status(ride: Dict[str, object], new_status: str) -> bool:
    new_status = new_status.strip().upper()
    current = str(ride.get("status", "WAITING")).upper()

    if new_status not in STATUS_FLOW:
        print("Invalid status")
        return False

    if current == new_status:
        return True

    allowed = {
        "WAITING": {"STARTED"},
        "STARTED": {"COMPLETED"},
        "COMPLETED": set(),
    }

    if new_status not in allowed.get(current, set()):
        print(f"Cannot change status {current} -> {new_status}")
        return False

    ride["status"] = new_status
    return True
