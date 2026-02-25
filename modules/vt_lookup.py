import requests
from config import VT_API_KEY

def check_vt(indicator):
    url = f"https://www.virustotal.com/api/v3/search?query={indicator}"
    
    headers = {
        "x-apikey": VT_API_KEY
    }

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        return {"malicious": False, "source": "VT error"}

    data = response.json()

    if "data" in data and len(data["data"]) > 0:
        return {"malicious": True, "source": "VirusTotal"}

    return {"malicious": False, "source": "VirusTotal"}