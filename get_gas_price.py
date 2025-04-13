import requests
import re
from bs4 import BeautifulSoup
def get_gas_price_st1():
    url = "https://bensinpriser.nu/stationer/95/vastra-gotalands-lan/goteborg"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    stations = []
    rows = soup.select("table tr")

    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 2:
            # Xử lý tên trạm: chèn khoảng trắng giữa chữ + số nếu cần
            raw_name = cols[0].get_text(strip=True)
            name_full = re.sub(r"([a-z])([A-Z])", r"\1 \2", raw_name)
            if "Göteborg" in name_full:
                # 2. Tách theo từ "Göteborg"
                parts = name_full.split("Göteborg", 1)

                name = parts[0].strip() + " Göteborg"
                address = parts[1].strip() + ", Göteborg" if len(parts) > 1 else "Göteborg"
                gg_address = parts[0].strip() + " " + address

                # Xử lý giá và ngày
                raw_price = cols[1].get_text(strip=True)
                match = re.match(r"([\d,]+kr)(\d{1,2}/\d{1,2})", raw_price)
                if match:
                    price, date = match.groups()
                else:
                    price, date = raw_price, "N/A"
                if "Gustaf" in address:
                    stations.append((name, address, price, date, gg_address))
                    break

        if len(stations) == 10:
            break
    return stations

def get_gas_price_10():
    url = "https://bensinpriser.nu/stationer/95/vastra-gotalands-lan/goteborg"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    stations = []
    rows = soup.select("table tr")

    for row in rows:
        cols = row.find_all("td")
        if len(cols) >= 2:
            # Xử lý tên trạm: chèn khoảng trắng giữa chữ + số nếu cần
            raw_name = cols[0].get_text(strip=True)
            name_full = re.sub(r"([a-z])([A-Z])", r"\1 \2", raw_name)
            if "Göteborg" in name_full:
                # 2. Tách theo từ "Göteborg"
                parts = name_full.split("Göteborg", 1)

                name = parts[0].strip() + " Göteborg"
                address = parts[1].strip() + ", Göteborg" if len(parts) > 1 else "Göteborg"
                gg_address = parts[0].strip() + " " + address

                # Xử lý giá và ngày
                raw_price = cols[1].get_text(strip=True)
                match = re.match(r"([\d,]+kr)(\d{1,2}/\d{1,2})", raw_price)
                if match:
                    price, date = match.groups()
                else:
                    price, date = raw_price, "N/A"
                # if "Gustaf" in address:
                #     stations.append((name, address, price, date))
                #     break
                stations.append((name, address, price, date, gg_address))

        if len(stations) == 10:
            break
    return stations

# result = get_gas_price()
# # In kết quả
# for i, (name, address, price, date) in enumerate(result, start=1):
#     print(f"{i}. Station: {name}, Address: {address}, 95 (E10): {price} (updated: {date})")
