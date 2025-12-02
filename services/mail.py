import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_ADDRESS = "amrulrahul@gmail.com"
EMAIL_PASSWORD = "bcrxzjfyfgaobasn"

def send_booking_email(to_email: str, name: str, flight_info: str):
    subject = "Konfirmasi Booking Tiket Anda"
    
    body = f"""
Hi {name},

Terima kasih telah melakukan pemesanan tiket.

Detail pesanan Anda:
- Maskapai: {flight_info}


Kami akan segera menghubungi Anda untuk proses berikutnya.

Salam hormat,
Telaga Amanah Travel
"""

    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)
