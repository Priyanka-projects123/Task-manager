import unittest
from task import Task


class TestTask(unittest.TestCase):

    def test_task_creation(self):
        task = Task("Task1", "Description", "High", "2026-12-31","Study")

        self.assertEqual(task.title, "Task1")
        self.assertEqual(task.description, "Description")
        self.assertEqual(task.priority, "High")
        self.assertEqual(task.due_date, "2026-12-31")
        self.assertEqual(task.category,"Study")
        self.assertFalse(task.completed)


if __name__ == "__main__":
    unittest.main()
