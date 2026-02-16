import json
from datetime import datetime
from task import Task

class TaskManager:
    def __init__(self, filename = 'tasks.json'):
        self.filename = filename
        self.tasks = []
        self.load_tasks()

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()

    def delete_task(self, index):
        self.tasks.pop(index)
        self.save_tasks()

    def mark_completed(self, index):
        self.tasks[index].completed = True
        self.save_tasks()

    def edit_task(self, index, title, description, priority, due_date):
        task = self.tasks[index]
        task.title = title
        task.description = description
        task.priority = priority
        task.due_date = due_date
        self.save_tasks()

    '''def analytics(self):
        total = len(self.tasks)
        completed = len([t for t in self.tasks if t.completed])
        pending = total - completed
        completion_percentage = (completed / total * 100) if total > 0 else 0
        today = datetime.today().date()
        overdue_tasks = []

        for task in self.tasks:
            if not task.completed:
               try:
                  due_date = datetime.strptime(task.due_date, "%Y-%m-%d").date()
                  if due_date < today:
                    overdue_tasks.append(task)
               except ValueError:
                   pass  # Ignore wrong date format

        return total, completed, pending, completion_percentage, overdue_tasks'''
    
    def filter_by_status(self, status):
       if status.lower() == "completed":
          return [t for t in self.tasks if t.completed]
       elif status.lower() == "pending":
          return [t for t in self.tasks if not t.completed]
       return []


    def filter_by_category(self, category):
       return [t for t in self.tasks if t.category.lower() == category.lower()]


    def filter_by_priority(self, priority):
       return [t for t in self.tasks if t.priority.lower() == priority.lower()]
    
    def sort_by_due_date(self):
       return sorted(self.tasks, key=lambda t: datetime.strptime(t.due_date, "%Y-%m-%d"))


    def sort_by_creation_date(self):
       return sorted(self.tasks, key=lambda t: datetime.strptime(t.created_at, "%Y-%m-%d %H:%M:%S"))


    def sort_by_priority(self):
       priority_order = {"High": 1, "Medium": 2, "Low": 3}
       return sorted(self.tasks, key=lambda t: priority_order.get(t.priority, 4))

          
    def save_tasks(self):
        with open(self.filename,'w') as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=4)

    def load_tasks(self):
        try:
            with open(self.filename,'r') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(t) for t in data]
        except FileNotFoundError:
            self.tasks = []
