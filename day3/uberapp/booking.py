from __future__ import annotations

from typing import Dict, List, Optional

import data
import drivers
import fare
import status


RIDES: List[Dict[str, object]] = []


def _canonical_location(user_text: str) -> Optional[str]:
    """Return the location with the same spelling from data.LOCATIONS."""

    user_n = data.normalize(user_text)
    for loc in data.LOCATIONS:
        if data.normalize(loc) == user_n:
            return loc
    return None


def _choose_location(label: str) -> Optional[str]:
    while True:
        query = input(f"Enter {label} location (or 0 to cancel): ").strip()
        if query == "0":
            return None

        canonical_direct = _canonical_location(query)
        if canonical_direct:
            return canonical_direct

        suggestions = data.suggest_locations(query, limit=5)
        if suggestions:
            print("Suggestions:")
            for idx, loc in enumerate(suggestions, start=1):
                print(f"  {idx}. {loc}")

            choice = input("Enter option number (or type location name): ").strip()
            if choice.isdigit():
                n = int(choice)
                if 1 <= n <= len(suggestions):
                    return suggestions[n - 1]

            manual = choice if choice else query
            canonical = _canonical_location(manual)
            if canonical:
                return canonical

        print("Location not found. Try again.")


def book_ride() -> None:
    print("\n--- Book a Ride ---")
    rider_name = input("Enter your name: ").strip()

    pickup = _choose_location("pickup")
    if pickup is None:
        print("Booking cancelled.")
        return

    drop = _choose_location("drop")
    if drop is None:
        print("Booking cancelled.")
        return

    # Pickup and drop should not be the same
    while data.normalize(drop) == data.normalize(pickup):
        print("Pickup and drop cannot be the same. Please enter a different drop location.")
        drop = _choose_location("drop")
        if drop is None:
            print("Booking cancelled.")
            return

    distance_km = data.get_distance_km(pickup, drop)

    assigned = drivers.assign_driver()
    if assigned is None:
        print("No drivers available. Please try later.")
        return

    driver_id, driver_info = assigned

    ride: Dict[str, object] = {
        "rider": rider_name,
        "pickup": pickup,
        "drop": drop,
        "route": (pickup, drop), 
        "driver": {"id": driver_id, **driver_info},
        "status": "WAITING",
        "distance_km": distance_km,
    }

    ride_fare = fare.calculate_fare(distance_km, base_fare=40, per_km=12, surge=1.0, discount=0.0)
    ride["fare"] = ride_fare

    RIDES.append(ride)

    print("\nBooking confirmed!")
    print(f"Pickup   : {pickup}")
    print(f"Drop     : {drop}")
    print(f"Driver   : {driver_info['name']} ({driver_info['vehicle']})")
    print(f"Status   : {ride['status']}")
    print(f"Distance : {distance_km} km")
    print(f"Fare     : ₹{ride_fare}")

    if input("Start ride now? (y/n): ").strip().lower() == "y":
        if status.update_status(ride, "STARTED"):
            print(f"Status updated: {ride['status']}")

    if input("Complete ride (Reached)? (y/n): ").strip().lower() == "y":
        if status.update_status(ride, "COMPLETED"):
            print("Successfully ride is completed!")
            print(f"Total Fare: ₹{ride['fare']}")
            drivers.release_driver(driver_id)
    else:
        print("Ride not completed yet. Use 'View Rides' to see status.")
