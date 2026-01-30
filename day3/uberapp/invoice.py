
from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

def _safe_name(text: str) -> str:
    keep = []
    for ch in text.strip():
        if ch.isalnum() or ch in {"-", "_"}:
            keep.append(ch)
        elif ch.isspace():
            keep.append("_")
    return "".join(keep) or "user"


def create_invoice(
    ride: Dict[str, object],
    *,
    invoice_dir: Optional[Path] = None,
    currency: str = "₹",
    **kwargs,
) -> Path:

    prefix = str(kwargs.get("prefix", "invoice"))

    here = Path(__file__).resolve().parent
    out_dir = invoice_dir or (here / "invoices")
    out_dir.mkdir(parents=True, exist_ok=True)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    rider = str(ride.get("rider", "user"))
    fname = f"{prefix}_{_safe_name(rider)}_{ts}.txt"
    path = out_dir / fname

    driver = ride.get("driver") or {}
    lines: List[str] = []
    lines.append("UBER APP - INVOICE")
    lines.append("=" * 30)
    lines.append(f"Rider    : {ride.get('rider')}")
    lines.append(f"Pickup   : {ride.get('pickup')}")
    lines.append(f"Drop     : {ride.get('drop')}")
    lines.append(f"Route    : {ride.get('route')}")
    lines.append(f"Driver   : {getattr(driver, 'get', lambda _k, _d=None: _d)('name', '-')}")
    lines.append(f"Vehicle  : {getattr(driver, 'get', lambda _k, _d=None: _d)('vehicle', '-')}")
    lines.append(f"Status   : {ride.get('status')}")
    lines.append(f"Distance : {ride.get('distance_km')} km")
    lines.append(f"Fare     : {currency}{ride.get('fare')}")
    lines.append("=" * 30)
    lines.append("Thank you for riding with us!")

    path.write_text("\n".join(lines), encoding="utf-8")
    return path
