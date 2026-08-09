# backend/services/report_storage.py
# The functions store raw report (save_report) and recommendation (save_decision)
# without docker, the generated files can be found in backend/reports/
# if docker compose is used, then the files will be stored in the docker container for backend
# docker compose exec backend ls reports

from pathlib import Path
from datetime import datetime
import json

REPORT_DIR = Path("reports")

REPORT_DIR.mkdir(exist_ok=True, parents=True)

def create_timestamp():
    return datetime.now().strftime("%Y%m%d_%H%M%S")

def save_report(company, report, timestamp):
    filename = (
        REPORT_DIR /
        f"{company}_{timestamp}.md"
    )
    with open(filename, "w", encoding="utf-8") as f:
        f.write(report)
    return str(filename)

def save_decision(company, decision, timestamp):
    filename = (
        REPORT_DIR /
        f"{company}_{timestamp}_decision.json"
    )
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(decision, f, indent=4, ensure_ascii=False)
    return str(filename)