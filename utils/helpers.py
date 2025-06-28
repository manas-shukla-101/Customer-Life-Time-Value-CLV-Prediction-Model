from typing import Any

def safe_str(obj: Any) -> str:
    """Safely convert any object to string, handling None."""
    if obj is None:
        return ""
    try:
        return str(obj)
    except Exception:
        return ""