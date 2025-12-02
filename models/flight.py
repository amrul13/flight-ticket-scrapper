from pydantic import BaseModel

class Flight(BaseModel):
    flight_name: str
    flight_id: str
    flight_code: str
    flight_from: str
    flight_to: str
    flight_route: str
    flight_date: str
    flight_datetime: str
    flight_transit: str
    flight_infotransit: str
    flight_price: int
    flight_image: str
    flight_baggage: str
    flight_facilities: str
    flight_duration: str
    display_price: int
    avail_seat: str
    adult: int
    child: int
    infant: int
