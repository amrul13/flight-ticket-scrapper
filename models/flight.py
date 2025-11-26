from pydantic import BaseModel

class Flight(BaseModel):
    flight_name: str
    flight_code: str
    flight_price: int
    flight_from: str
    flight_to: str
    flight_route: str
    flight_date: str
    flight_datetime: str
    flight_transit: str
    flight_infotransit: str
    flight_image: str
    flight_baggage: str
    flight_facilities: str
    flight_duration: str
    adult: int
    child: int
    infant: int
