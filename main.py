import json
import urllib.request

url = "https://api.digital.rema1000.dk/api/v3/products?include=department&sort=department_order&filter[is_advertised]=true&per_page=500"

req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})

with urllib.request.urlopen(req) as response:
    data = json.loads(response.read().decode("utf-8"))

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f)

print("Saved raw API payload to data.json")
