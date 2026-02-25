from modules.vt_lookup import check_vt
from modules.abuse_lookup import check_abuse
from modules.decision_engine import check_blacklist
from modules.logger import log_incident

def analyze(indicator):

    vt = check_vt(indicator)
    abuse = check_abuse(indicator) if "." in indicator else {"malicious": False}
    blacklist = check_blacklist(indicator)

    if vt["malicious"] or abuse["malicious"] or blacklist:
        verdict = "ESCALATE — MALICIOUS"
        action = "Simulating firewall block..."
    else:
        verdict = "AUTO-RESOLVED — SAFE"
        action = "No action required."

    print("\n--- SOAR RESULT ---")
    print(f"Indicator: {indicator}")
    print(f"Verdict: {verdict}")
    print(action)

    log_incident(indicator, verdict)


if __name__ == "__main__":
    indicator = input("Enter IP / Domain / Hash: ")
    analyze(indicator)