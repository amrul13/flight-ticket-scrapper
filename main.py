from fastapi import FastAPI
from routers import flights
from functools import lru_cache
from services.sheet import append_order
from services.telegram import send_telegram
from services.telegram import format_telegram_message
from services.mail import send_booking_email
from models.order import Order



import requests

from fastapi.middleware.cors import CORSMiddleware






app = FastAPI(
    title="Telaga Amanah Travel API",
    description="API pencarian tiket pesawat",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # sementara * dulu
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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

@app.post("/order")
def make_order(payload: Order):

    # Simpan ke Google Sheet
    append_order(payload)

    # Kirim notifikasi telegram
    formatted_message = format_telegram_message(payload)
    send_telegram(formatted_message) 

    return {"status": "success", "message": "Order berhasil disimpan."}