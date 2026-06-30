# Mini SOAR Playbook in Python

A lightweight Security Orchestration, Automation, and Response (SOAR) simulation that automates phishing and IOC (Indicator of Compromise) analysis using multiple threat intelligence sources.

This project replicates a real SOC (Security Operations Center) workflow by enriching suspicious indicators, applying decision logic, and automating response actions.

---

## Features

- Threat intelligence enrichment via VirusTotal API
- IP reputation lookup using AbuseIPDB
- Local blacklist correlation
- Rule-based decision engine (Escalate vs Auto-resolve)
- Automated incident logging
- Simulated containment action

---

## How It Works

1. User provides a suspicious:
   - IP address
   - Domain
   - File hash

2. The system:
   - Queries VirusTotal
   - Checks AbuseIPDB (for IPs)
   - Compares against local blacklist

3. Decision Logic:
   - If any source flags malicious → ESCALATE
   - If clean → AUTO-RESOLVED

4. Incident is logged to `logs/incidents.log`

---

## 📁 Project Structure

mini-soar/
│
├── soar.py
├── config.py
├── blacklist.txt
├── logs/
│   └── incidents.log
└── modules/
    ├── vt_lookup.py
    ├── abuse_lookup.py
    ├── decision_engine.py
    └── logger.py

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/mini-soar.git
cd mini-soar
```

2.Install dependencies:

```bash
pip install requests
```

3.Add your API keys in config.py:

```bash
VT_API_KEY = "your_virustotal_key"
ABUSE_API_KEY = "your_abuseipdb_key"
```
## Usage
Run the script:

```bash
python3 soar.py
```
Example Output:
```bash
--- SOAR RESULT ---
Indicator: 192.168.x.x
Verdict: ESCALATE — MALICIOUS
Simulating firewall block...
```

