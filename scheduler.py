import schedule
import time
from datetime import datetime
from date_parser import parse_due_date
from db import get_pending_tasks

def send_reminder(title, due_date):
    print(f"\n🔔 Reminder: {title} (Due: {due_date})\n")

def schedule_reminder(title, due_date):
    dt = parse_due_date(due_date)
    if not dt:
        return
    
    schedule_time = dt.strftime("%H:%M")


    if dt.date() >= datetime.now().date():
        schedule.every().day.at(schedule_time).do(
            send_reminder, title=title, due_date=due_date
        )

def daily_summary(conn):
    tasks = get_pending_tasks(conn)
    print("\n------ DAILY SUMMARY ------")
    if not tasks:
        print("No pending tasks.")
        return
    for t in tasks:
        print(f"{t[0]}. {t[1]} | Due: {t[2]} | Priority: {t[3]} | Category: {t[4]}")
    print()

def start_scheduler(conn):

    schedule.every().day.at("09:00").do(daily_summary, conn)

    while True:
        schedule.run_pending()
        time.sleep(1)
