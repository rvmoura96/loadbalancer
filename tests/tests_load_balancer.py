# flake8: noqa
from unittest import TestCase

from load_balancer import LoadBalancer
from server import Server
from user import User


class TestLoadBalancer(TestCase):
    def setUp(self) -> None:
        self.load_balancer = LoadBalancer(4, 2)

    def test_create_a_server_should_return_a_server_instance(self):
        server = self.load_balancer.create_a_server()
        self.assertIsInstance(server, Server)

    def test_verify_available_server_existance_should_return_false_without_servers_created(self):
        expected = False
        result = self.load_balancer.verify_available_server_existence()
        self.assertEqual(expected, result)

    def test_verify_available_server_existance_should_return_true_when_has_a_server_available(self):
        exptected = True
        server = self.load_balancer.create_a_server()
        self.load_balancer.servers.append(server)

        result = self.load_balancer.verify_available_server_existence()
        self.assertEqual(exptected, result)

    def test_calculate_total_should_return_three_when_there_are_three_servers_running_on_load_balancer(self):
        for i in range(3):
            server = self.load_balancer.create_a_server()
            user = User(1)
            server.connect(user)
            self.load_balancer.servers.append(server)

        expected = 3
        result = self.load_balancer.calculate_total()
        self.assertEqual(expected, result)
