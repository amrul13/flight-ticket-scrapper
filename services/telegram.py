import requests
import os

from models.order import Order

# Menggunakan placeholder untuk token dan ID yang sensitif
# (Diasumsikan Anda akan memuatnya dari .env pada aplikasi final Anda)
BOT_TOKEN = "1146754332:AAHUp1_fX6HPVCyd5VyZC-1W-3abiFfkW_w"
CHANNEL_ID_PROD = "-1003391205547"
# CHANNEL_ID = "-1003466970817"

def format_telegram_message(data: Order) -> str:
    """Membuat pesan Telegram dengan format Markdown yang rapi."""
    
    message = f"""
✨ **PESANAN TIKET BARU MASUK!**
---
🔔 **RINGKASAN ORDER**
*Total Pembayaran:* **Rp {data.total}**
*Tanggal Booking:* {data.timestamp.split("T")[0]}
---

👤 **DETAIL PENUMPANG**
*Nama:* **{data.passenger.get("fullName", "N/A")}**
*Kontak:* `{data.passenger.get("phone", "N/A")}`
*Email:* `{data.passenger.get("email", "N/A")}`
*Tanggal Lahir:* {data.passenger.get("birthDate", "N/A")}
*NIK:* {data.passenger.get("nik", "N/A")}

✈️ **DETAIL PENERBANGAN**
*Kode:* **{data.flight.get("flight_code", "N/A")}**
*Rute Utama:* **{data.flight.get("flight_from", "N/A")}** ➡️ **{data.flight.get("flight_to", "N/A")}**
*Tanggal Penerbangan:* {data.flight.get("flight_date", "N/A")}
*Rute:* _{data.flight.get("flight_infotransit", "N/A") if data.flight.get("flight_infotransit") else "Langsung"}_
"""
    # send_booking_email(
    #     to_email=data["email"],
    #     name=data["name"],
    #     flight_info=data["flight_code"]
    # )
    return message

def send_telegram(message: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHANNEL_ID_PROD,
        # "chat_id": CHANNEL_ID,
        "text": message,
        "parse_mode": "Markdown" 
    }
    
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status() # Cek error HTTP
        # print(f"Telegram status: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to send Telegram notification: {e}")