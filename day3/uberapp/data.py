
from __future__ import annotations

from typing import Dict, List, Tuple


LOCATIONS: List[str] = [
    "kOMPALLY",
    "KANDLAKOYA",
    "MEDCHAL",
    "IDPL",
    "BALANAGAR",
    "Miyapur",
    "Ameerpet",
    "Begumpet",
]


LOCATION_SET = set(LOCATIONS)


def normalize(text: str) -> str:
    return " ".join(text.strip().lower().split())


def suggest_locations(query: str, *, limit: int = 5, **kwargs) -> List[str]:

    starts_with = bool(kwargs.get("starts_with", False))
    q = normalize(query)
    if not q:
        return LOCATIONS[:limit]

    matches: List[str] = []
    for loc in LOCATIONS:
        loc_n = normalize(loc)
        ok = loc_n.startswith(q) if starts_with else (q in loc_n)
        if ok:
            matches.append(loc)
    return matches[:limit]


def route_key(pickup: str, drop: str) -> Tuple[str, str]:
    """Make a stable tuple key for a route regardless of direction."""

    a = normalize(pickup)
    b = normalize(drop)
    return (a, b) if a <= b else (b, a)


DISTANCE_KM: Dict[Tuple[str, str], int] = {
    route_key("kOMPALLY", "KANDLAKOYA"): 6,
    route_key("kOMPALLY", "MEDCHAL"): 8,
    route_key("kOMPALLY", "IDPL"): 10,
    route_key("kOMPALLY", "BALANAGAR"): 15,
    route_key("kOMPALLY", "Miyapur"): 12,
    route_key("kOMPALLY", "AMEERPET"): 14,
    route_key("kOMPALLY", "BEGUMPET"): 13,

    route_key("KANDLAKOYA", "MEDCHAL"): 7,
    route_key("KANDLAKOYA", "IDPL"): 9,
    route_key("KANDLAKOYA", "BALANAGAR"): 14,
    route_key("KANDLAKOYA", "Miyapur"): 11,
    route_key("KANDLAKOYA", "AMEERPET"): 13,
    route_key("KANDLAKOYA", "BEGUMPET"): 12,

    route_key("MEDCHAL", "IDPL"): 4,
    route_key("IDPL", "BALANAGAR"): 11,
    route_key("IDPL", "Miyapur"): 8,
    route_key("IDPL", "AMEERPET"): 10,
    route_key("IDPL", "BEGUMPET"): 9,
    route_key("BALANAGAR", "Miyapur"): 3,
    route_key("BALANAGAR", "AMEERPET"): 5,
    
    route_key("BALANAGAR", "BEGUMPET"): 6,
    route_key("Miyapur", "AMEERPET"): 4,
    route_key("Miyapur", "BEGUMPET"): 5,
    route_key("AMEERPET", "MEDCHAL"): 9,
    route_key("AMEERPET", "BEGUMPET"): 2,
    route_key("BEGUMPET", "MEDCHAL"): 8,
    route_key("BEGUMPET", "Miyapur"): 5,
    route_key("Miyapur", "BALANAGAR"): 6,
    route_key("MEDCHAL", "KANDLAKOYA"): 7,

}


def get_distance_km(pickup: str, drop: str) -> int:

    if normalize(pickup) == normalize(drop):
        return 0
    return DISTANCE_KM.get(route_key(pickup, drop), 5)
