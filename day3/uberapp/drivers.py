"""Driver data + assignment.

Uses dict, set, tuple.
"""

from __future__ import annotations

from typing import Dict, Optional, Tuple


DRIVERS: Dict[str, Dict[str, object]] = {
    "D1": {"name": "Arun", "vehicle": "TS16EB-8343"},
    "D2": {"name": "Maruti", "vehicle": "TS09CD-1234"},
    "D3": {"name": "Ravi", "vehicle": "TS07AA-5678"},
}

AVAILABLE_DRIVERS = set(DRIVERS.keys())

def assign_driver(*, preferred_id: Optional[str] = None, **kwargs) -> Optional[Tuple[str, Dict[str, object]]]:
    
    allow_any = bool(kwargs.get("allow_any", True))

    if preferred_id and preferred_id in AVAILABLE_DRIVERS:
        AVAILABLE_DRIVERS.remove(preferred_id)
        return preferred_id, DRIVERS[preferred_id]

    if not allow_any:
        return None

    if not AVAILABLE_DRIVERS:
        return None

    driver_id = sorted(AVAILABLE_DRIVERS)[0]
    AVAILABLE_DRIVERS.remove(driver_id)
    return driver_id, DRIVERS[driver_id]


def release_driver(driver_id: str) -> None:
    if driver_id in DRIVERS:
        AVAILABLE_DRIVERS.add(driver_id)
