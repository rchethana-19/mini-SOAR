import requests
from config import ABUSE_API_KEY

def check_abuse(ip):
    url = "https://api.abuseipdb.com/api/v2/check"
    
    params = {
        "ipAddress": ip,
        "maxAgeInDays": 90
    }

    headers = {
        "Key": ABUSE_API_KEY,
        "Accept": "application/json"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return {"malicious": False, "confidence": 0}

    data = response.json()
    score = data["data"]["abuseConfidenceScore"]

    return {"malicious": score > 50, "confidence": score}