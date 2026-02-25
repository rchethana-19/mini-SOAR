from datetime import datetime

def log_incident(indicator, verdict):
    with open("logs/incidents.log", "a") as f:
        f.write(f"{datetime.now()} | {indicator} | {verdict}\n")