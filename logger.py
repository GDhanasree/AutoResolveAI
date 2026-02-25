# logger.py

import os
import pandas as pd
from datetime import datetime

LOG_FILE = "data/active_log.csv"

def initialize_log():
    """
    Creates log file if it doesn't exist
    """
    if not os.path.exists(LOG_FILE):
        df = pd.DataFrame(columns=[
            "timestamp",
            "ticket_text",
            "predicted_issue",
            "confidence",
            "automation_result",
            "status"
        ])
        df.to_csv(LOG_FILE, index=False)


def log_ticket(ticket, prediction, confidence, result, status):
    """
    Appends a new log entry
    """
    initialize_log()

    new_entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ticket_text": ticket,
        "predicted_issue": prediction,
        "confidence": round(confidence * 100, 2),
        "automation_result": result,
        "status": status
    }

    df = pd.read_csv(LOG_FILE)
    df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)
    df.to_csv(LOG_FILE, index=False)