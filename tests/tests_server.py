# flake8: noqa
from unittest import TestCase

from server import Server
from user import User


class TestServer(TestCase):
    def setUp(self) -> None:
        self.server = Server(umax=4)

    def test_available_should_return_true_when_server_has_no_users(self):
        expected = True
        result = self.server.available()
        self.assertEqual(expected, result)

    def test_available_should_return_false_when_server_has_users_len_equal_to_umax_attribute(self):
        for i in range(self.server.umax):
            self.server.connect(User(i))

        expected = False
        result = self.server.available()
        self.assertEqual(expected, result)

    def test_total_users_should_return_one_when_server_has_only_one_user_online(self):
        self.server.connect(User(1))
        expected = 1
        result = self.server.total_users()
        self.assertEqual(expected, result)

    def test_after_disconect_a_user_with_a_task_complete_the_users_len_should_be_zero(self):
        self.server.connect(User(0))
        self.server.disconnect()
        expected = 0
        result = self.server.total_users()
        self.assertEqual(expected, result)

    def test_after_calculate_total_per_tick_once_runned_server_total_should_be_three(self):
        self.server.connect(User(1))
        self.server.connect(User(1))
        self.server.connect(User(1))
        self.server.calculate_total_per_tick()
        expected = 3
        result = self.server.total
        self.assertEqual(expected, result)

    def test_after_two_ticks_calculate_with_three_users_server_total_attribute_should_be_six(self):
        self.server.connect(User(1))
        self.server.connect(User(1))
        self.server.connect(User(1))
        self.server.calculate_total_per_tick()
        self.server.calculate_total_per_tick()
        expected = 6
        result = self.server.total
        self.assertEqual(expected, result)
