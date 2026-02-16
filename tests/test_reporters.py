import unittest
from task import Task
from reporters import calculate_analytics


class TestReporters(unittest.TestCase):

    def test_analytics_calculation(self):
        tasks = [
            Task("Task1", "Desc", "High", "2026-12-31","Study"),
            Task("Task2", "Desc", "Low", "2026-12-30","Study")
        ]

        tasks[0].completed = True

        total, completed, pending, percentage, overdue_tasks = calculate_analytics(tasks)

        self.assertEqual(total, 2)
        self.assertEqual(completed, 1)
        self.assertEqual(pending, 1)
        self.assertEqual(percentage,50.0)


if __name__ == "__main__":
    unittest.main()
