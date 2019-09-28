from unittest import TestCase

from load_balancer import Task


class TestTask(TestCase):
    def setUp(self) -> None:
        self.task = Task(ticks_to_conclusion=4)

    def test_after_call_execute_method_ticks_to_conclusion_should_be_3(self):
        self.task.execute()
        expected = 3
        result = self.task.ticks_to_conclusion
        self.assertEqual(expected, result)

    def test_complete_method_should_return_false_when_task_ticks_to_conclusion_is_greater_than_zero(self):
        self.task.execute()
        expected = False
        result = self.task.complete
        self.assertEqual(expected, result)

    def test_complete_method_should_return_true_when_ticks_to_conclusion_is_equal_zero(self):
        for i in range(self.task.ticks_to_conclusion):
            self.task.execute()
        expected = True
        result = self.task.complete
        self.assertEqual(expected, result)