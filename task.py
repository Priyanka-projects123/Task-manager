from datetime import datetime

class Task:
    def __init__(self, title, description, priority, due_date, category):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.category = category
        self.completed = False
        self.created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    def to_dict(self):
        return {
        'title' : self.title,
        'description' : self.description,
        'priority' : self.priority,
        'due_date' : self.due_date,
        'category' : self.category,
        'completed' : self.completed,
        'created_at' : self.created_at
        } 
    
    @staticmethod
    def from_dict(data):
        task = Task(data['title'], data['description'], data['priority'], data['due_date'], data.get('category',"General"))
        task.completed = data.get(('completed',False))
        task.created_at = data.get(('created_at',""))
        return task
