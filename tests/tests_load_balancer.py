# flake8: noqa
from unittest import TestCase

from load_balancer import LoadBalancer
from server import Server


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

