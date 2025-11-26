import requests
from bs4 import BeautifulSoup

url = "https://klikmbc.biz/v2/form_flight_result_cari?flight_from=Jakarta%20(CGK)&flight_to=Denpasar%20(DPS)&goback=0&flight_dateback=&dewasa_number=1&anak_number=0&bayi_number=0&dewasa=1&anak=0&bayi=0&flight_datedeparture=Senin,%2024%20Nov%202025"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Referer": "https://klikmbc.biz/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive"
}

res = requests.get(url, headers=headers)

with open("debug.html", "w", encoding="utf-8") as f:
    f.write(res.text)

soup = BeautifulSoup(res.text, "html.parser")

# setiap item penerbangan = 1 form
forms = soup.find_all("form", id=lambda v: v and v.startswith("form_"))

result = []

for form in forms:
    # Harga
    price = form.select_one(".tvl-price")
    price = price.get_text(strip=True) if price else None

    # Jam berangkat
    dep_time = form.select_one(".tvl-content-top span")
    dep_time = dep_time.get_text(strip=True) if dep_time else None

    # Durasi
    duration = form.select_one(".tvl-duration")
    duration = duration.get_text(strip=True) if duration else None

    # Jam tiba
    arr_time = form.select_one(".tvl-departure-time")
    arr_time = arr_time.get_text(strip=True) if arr_time else None

    # Maskapai
    flight_name_tag = form.find("input", {"name": "flight_name"})
    airline = flight_name_tag["value"]

    # Hasil: 'Sriwijaya'

    # Kode flight (input hidden)
    flight_code = form.find("input", {"name": "flight_code"})
    flight_code = flight_code["value"] if flight_code else None

    # Bandara Asal & Tujuan
    org_dest = form.select(".tvl-box-org-dest")
    origin = org_dest[0].get_text(strip=True) if len(org_dest) > 0 else None
    dest = org_dest[1].get_text(strip=True) if len(org_dest) > 1 else None

    result.append({
        "maskapai": airline,
        "kode_flight": flight_code,
        "berangkat": dep_time,
        "tiba": arr_time,
        "durasi": duration,
        "dari": origin,
        "ke": dest,
        "harga": price
    })

for r in result:
    print(r)
