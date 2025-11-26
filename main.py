from fastapi import FastAPI
from routers import flights
from functools import lru_cache

import requests


app = FastAPI(
    title="Telaga Amanah Travel API",
    description="API pencarian tiket pesawat berbasis scrapping",
    version="1.0.0"
)

app.include_router(flights.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "Telaga Amanah Travel API running"}

@lru_cache(maxsize=1)
def fetch_codes():
    url = "https://klikmbc.co.id/json/getcodearea-json"
    return requests.get(url).json()

@app.get("/area-codes")
def area_codes():
    return {"results": fetch_codes()}