from task import Task
from task_manager import TaskManager
from validators import (
    validate_required,
    validate_priority,
    validate_category,
    validate_date,
    validate_index
)
from reporters import calculate_analytics


def display_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return
    
    print("\n ---- Task List ---- ")
    for index, task in enumerate(tasks, start = 1):
        status = "Completed" if task.completed else "Pending"
        print(f"{index}.{task.title} | {task.priority} | Due:- {task.due_date} | {status}")

def main():
    manager = TaskManager()
    while True:
        print("\n ==== Task Manager Menu ==== \n")
        print("1. Add Task. \n2. View all Tasks. \n3. Mark Task as Completed. \n4. Edit Task. \n5. Delete Task. ")
        print("6. View Analytics. \n7. Filter tasks. \n8. Sort tasks. \n9. View tasks by.... \n10. Exit")
        choice = input("Enter your choice (1-7) :-  ")
           # Add task
        if choice == '1':
            title = input("Enter task title:- ")
            description = input("Enter task description:- ")
            priority = input("Enter priority ( High / Medium / Low ):- ")
            due_date = input("Enter due date ( YYYY-MM-DD ):- ")
            category = input("Enter category (Work/Personal/Study/etc):- ")
            task = Task(title, description, priority, due_date, category)
            manager.add_task(task)
            print("\n Task added Successfully.")

            # View tasks
        elif choice == '2':
            display_tasks(manager.tasks)
            # Mark task as completed
        elif choice == '3':
           display_tasks(manager.tasks)
           index = int(input("Enter task number to mark as completed :- ")) - 1
           manager.mark_completed(index)
           print("\n Task mark as completed.")

           # Edit task
        elif choice == '4':
            display_tasks(manager.tasks)
            index = int(input("Enter task number to edit :- ")) - 1
            title = input("New title:- ")
            description = input("New description:- ")
            priority = input("New priority ( High / Medium / Low ):- ")
            due_date = input("New due date ( YYYY-MM-DD ):- ") 
            manager.edit_task(index, title, description, priority, due_date)
            print("\n Task updated successfully. ")

            # Delete task
        elif choice == '5':
            index = int(input("Enter task number to delete :- ")) - 1
            manager.delete_task(index)
            print("\n Task deleted successfully. ")

            # Analytics
        elif choice == '6':
            calculate_analytics(manager.tasks)

               # Filtering
        elif choice == '7':
            print("1. Filter by Status")
            print("2. Filter by Category")
            print("3. Filter by Priority")
            sub = input("Choose option:- ")

            if sub == '1':
               status = input("Enter status (Completed/Pending):- ")
               display_tasks(manager.filter_by_status(status))

            elif sub == '2':
                category = input("Enter category:- ")
                display_tasks(manager.filter_by_category(category))

            elif sub == '3':
                priority = input("Enter priority (High/Medium/Low):- ")
                display_tasks(manager.filter_by_priority(priority))

                # Sorting
        elif choice == '8':
            print("1. Sort by Due Date")
            print("2. Sort by Priority")
            print("3. Sort by Creation Date")
            sub = input("Choose option:- ")

            if sub == '1':
                display_tasks(manager.sort_by_due_date())

            elif sub == '2':
                display_tasks(manager.sort_by_priority())

            elif sub == '3':
                display_tasks(manager.sort_by_creation_date())

                # View tasks by different types
        elif choice == '9':
            print("\n--- View Tasks By ---\n")
            print("1. Category")
            print("2. Status")
            print("3. Priority")

            sub = input("Choose option: ")

            if sub == '1':
                category = input("Enter category: ")
                tasks = manager.filter_by_category(category)
                display_tasks(tasks)

            elif sub == '2':
                status = input("Enter status (Completed/Pending): ")
                tasks = manager.filter_by_status(status)
                display_tasks(tasks)

            elif sub == '3':
                priority = input("Enter priority (High/Medium/Low): ")
                tasks = manager.filter_by_priority(priority)
                display_tasks(tasks)

            else:
               print("Invalid option.")

            # Exit 
        elif choice == '10':
            print("\n Exiting the task manager...... ")
            break
        else:
            print(" Invalid Choice ! Please enter a number between 1 and 7")

if __name__ == "__main__":
    main()        

