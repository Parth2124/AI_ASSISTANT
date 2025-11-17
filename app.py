import threading
from gemini_nlp import parse_task, break_down_task
from db import init_db, add_task, get_pending_tasks, get_completed_tasks, complete_task
from scheduler import start_scheduler, schedule_reminder

def main():
    print("\n=== AI Task Manager Started ===\n")
    conn = init_db()

    threading.Thread(target=start_scheduler, args=(conn,), daemon=True).start()

    print("Commands:")
    print(" - Add tasks by typing naturally")
    print(" - break down <task>")
    print(" - list pending")
    print(" - list done")
    print(" - mark done <task_id>")
    print(" - exit / quit\n")

    while True:
        user_in = input("> ").strip()

        # Exit
        if user_in.lower() in ["exit", "quit"]:
            print("Exiting Task Manager...")
            break


        if user_in.lower() == "list pending":
            tasks = get_pending_tasks(conn)
            print("\nPending Tasks:")
            if not tasks:
                print("No pending tasks.\n")
            else:
                for t in tasks:
                    print(f"{t[0]}. {t[1]} | Due: {t[2]} | Priority: {t[3]} | Category: {t[4]}")
                print()
            continue


        if user_in.lower() == "list done":
            tasks = get_completed_tasks(conn)
            print("\nCompleted Tasks:")
            if not tasks:
                print("No completed tasks.\n")
            else:
                for t in tasks:
                    print(f"{t[0]}. {t[1]}")
                print()
            continue


        if user_in.lower().startswith("mark done"):
            try:
                task_id = int(user_in.split()[2])
                complete_task(conn, task_id)
                print(f"Task {task_id} marked as done.\n")
            except:
                print("Usage: mark done <task_id>\n")
            continue


        if user_in.lower().startswith("break down"):
            task_text = user_in[10:].strip()
            if not task_text:
                print("Please provide a task to break down.\n")
                continue
            subtasks = break_down_task(task_text)
            if "error" in subtasks:
                print("Error:", subtasks, "\n")
            else:
                print("\nSubtasks:")
                for i, st in enumerate(subtasks, 1):
                    print(f"{i}. {st}")
                print()
            continue


        parsed = parse_task(user_in)

        if "error" in parsed:
            print("\nModel Error:", parsed, "\n")
            continue

        add_task(
            conn,
            parsed.get("title"),
            parsed.get("due_date"),
            parsed.get("priority"),
            parsed.get("category")
        )

        title = parsed.get('title')
        due_date = parsed.get('due_date')

        print(f"\nTask added: {title}")

        if due_date and due_date.lower() != "null":
            schedule_reminder(title, due_date)
            print(f"Reminder scheduled for: {due_date}\n")
        else:
            print()

if __name__ == "__main__":
    main()
