import requests
from bs4 import BeautifulSoup

def scrape_flights(url: str):
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "Referer": "https://klikmbc.biz/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Connection": "keep-alive"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    

    flights = []
    forms = soup.find_all("form", id=lambda x: x and x.startswith("form_"))

    for form in forms:
        data = {}
        hidden_inputs = form.find_all("input", type="hidden")

        for inp in hidden_inputs:
            name = inp.get("name")
            value = inp.get("value")
            data[name] = value

        # harga tampilannya ada di span.tvl-price
        price_tag = form.select_one("span.tvl-price")
        if price_tag:
            data["display_price"] = price_tag.get_text(strip=True)

        flights.append(data)

    return flights