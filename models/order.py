from pydantic import BaseModel
from typing import Dict
from typing import Any

class Order(BaseModel):
    bookingRef: str
    flight: Dict[str, Any]
    passenger: Dict[str, Any]
    total: int
    timestamp: str