import gspread
from models.order import Order
from google.oauth2.service_account import Credentials

# scopes API google sheets
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive"
]

creds = Credentials.from_service_account_file("service_account.json", scopes=SCOPES)
client = gspread.authorize(creds)

# masukkan ID spreadsheet kamu
SHEET_ID = "1kFK-f9iO0sIozAZ0jv9q5QBtSCaCCazRmRjXtCQOVls"

def append_order(data: Order):
    print(data.flight)
    sheet = client.open_by_key(SHEET_ID).sheet1
    row = [
        data.passenger.get("fullName"),
        data.passenger.get("birthDate"),
        data.passenger.get("phone"),
        data.passenger.get("email"),
        data.passenger.get("nik"),
        data.flight.get("flight_from"),
        data.flight.get("flight_to"),
        data.bookingRef,
        data.timestamp.split("T")[0],
        data.flight.get("flight_date"),
        data.flight.get("flight_name"),
        data.flight.get("flight_code"),
        data.total,
        "Menunggu Pembayaran",
    ]
    sheet.append_row(row)
