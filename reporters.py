from datetime import datetime


def calculate_analytics(tasks):
    total = len(tasks)
    completed = len([t for t in tasks if t.completed])
    pending = total - completed

    percentage = (completed / total * 100) if total > 0 else 0

    today = datetime.today().date()
    overdue_tasks = []

    for task in tasks:
        if not task.completed:
            try:
                due_date = datetime.strptime(task.due_date, "%Y-%m-%d").date()
                if due_date < today:
                    overdue_tasks.append(task)
            except ValueError:
                pass

           
    print("\n--- Analytics Report ---")
    print(f"Total tasks: {total}")
    print(f"Completed tasks: {completed}")
    print(f"Pending tasks: {pending}")
    print(f"Completion Percentage: {percentage:.2f}%")

    if overdue_tasks:
        print("\n⚠ Overdue Tasks Alert:")
        for task in overdue_tasks:
            print(f"- {task.title} (Due: {task.due_date})")
    else:
        print("\nNo overdue tasks.")
    
    return total, completed, pending, percentage, overdue_tasks

