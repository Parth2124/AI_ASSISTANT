from datetime import datetime, timedelta
import re

def parse_due_date(due):
    due = due.lower().strip()
    now = datetime.now()


    if due in [None, "", "null"]:
        return None

    if "tomorrow" in due:
        dt = now + timedelta(days=1)
    elif "today" in due:
        dt = now
    else:
        # Weekday parsing
        days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
        for i, d in enumerate(days):
            if d in due:
                today_idx = now.weekday()
                target = i
                diff = (target - today_idx) % 7
                dt = now + timedelta(days=diff)
                break
        else:
            # fallback: 1 hour from now
            return now + timedelta(hours=1)


    if "morning" in due:
        return dt.replace(hour=9, minute=0, second=0)
    if "afternoon" in due:
        return dt.replace(hour=14, minute=0, second=0)
    if "evening" in due:
        return dt.replace(hour=18, minute=0, second=0)

    # Default time: 10 AM
    return dt.replace(hour=10, minute=0, second=0)
