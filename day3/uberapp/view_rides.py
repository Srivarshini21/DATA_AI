
from __future__ import annotations

import booking
import invoice


def view_rides() -> None:
    if not booking.RIDES:
        print("No rides booked yet.")
        return

    print("\n--- YOUR RIDES ---")
    for i, ride in enumerate(booking.RIDES, start=1):
        route = ride.get("route")
        driver = ride.get("driver") or {}
        print(
            f"{i}. {ride.get('pickup')} -> {ride.get('drop')} | "
            f"Driver: {driver.get('name', '-') } | "
            f"Status: {ride.get('status')} | Fare: ₹{ride.get('fare')}"
        )
    print("-------------------\n")

    latest_ride = booking.RIDES[-1]
    saved_path = invoice.create_invoice(latest_ride)
    print(f"Invoice downloaded: {saved_path}")
