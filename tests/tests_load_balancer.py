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
