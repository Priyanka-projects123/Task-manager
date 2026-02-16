import unittest
from task_manager import TaskManager
from task import Task


class TestTaskManager(unittest.TestCase):

    def setUp(self):
        self.manager = TaskManager()
        self.manager.tasks = []  # Clear existing tasks

    def test_add_task(self):
        task = Task("Task1", "Desc", "High", "2026-12-31","Study")
        self.manager.add_task(task)

        self.assertEqual(len(self.manager.tasks), 1)

    def test_delete_task(self):
        task = Task("Task1", "Desc", "High", "2026-12-31","Study")
        self.manager.add_task(task)

        self.manager.delete_task(0)

        self.assertEqual(len(self.manager.tasks), 0)


if __name__ == "__main__":
    unittest.main()
