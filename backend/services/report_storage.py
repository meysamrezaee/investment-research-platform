# backend/services/report_storage.py

from pathlib import Path
from datetime import datetime
import json

REPORT_DIR = Path("reports")

REPORT_DIR.mkdir(exist_ok=True)


def create_timestamp():

    return datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )


def save_report(
    company,
    report
):

    timestamp = create_timestamp()

    filename = (
        REPORT_DIR /
        f"{company}_{timestamp}.md"
    )

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(report)

    return str(filename)


def save_decision(
    company,
    decision
):

    timestamp = create_timestamp()

    filename = (
        REPORT_DIR /
        f"{company}_{timestamp}_decision.json"
    )

    with open(
        filename,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            decision,
            f,
            indent=4
        )

    return str(filename)