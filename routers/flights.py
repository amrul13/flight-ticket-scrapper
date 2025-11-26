from fastapi import APIRouter, Query
from services.scraper import scrape_flights
from models.flight import Flight
from typing import List
from urllib.parse import quote


router = APIRouter()

@router.get("/flights", response_model=List[Flight])
def get_flights(
    from_city: str = Query(..., description="Contoh: Jakarta (CGK)"),
    to_city: str = Query(..., description="Contoh: Denpasar (DPS)"),
    date: str = Query(..., description="Contoh: Rabu, 26 Nov 2025")
):
    from_encoded = quote(from_city)
    to_encoded = quote(to_city)
    date_encoded = quote(date)

    url = (
        "https://klikmbc.biz/v2/form_flight_result_cari?"
        f"flight_from={from_encoded}"
        f"&flight_to={to_encoded}"
        f"&goback=0"
        f"&flight_dateback="
        f"&dewasa=1"
        f"&anak=0"
        f"&bayi=0"
        f"&flight_datedeparture={date_encoded}"
    )

    print(url)

    return scrape_flights(url)
