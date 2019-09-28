from server import Server
from user import User


class LoadBalancer:
    def __init__(self, ttask: int, umax: int):
        self.TTASK = ttask
        self.UMAX = umax
        self.servers = list()
        self.total = int()

    def calculate_total(self) -> int:
        """"Calculate the total cost of all servers.

        Calculate the total cost of all servers on servers
        attributes.
        """
        for server in self.servers:
            self.total += server.calculate_total_per_tick()

    def verify_available_server_existence(self) -> bool:
        """Verify the existence of a available server.

        Verify the existence of a available server on
        servers attributes.
        """
        for server in self.servers:
            if server.available():
                return True
        return False

    def create_a_server(self) -> Server:
        """"Create a server instance."""
        server = Server(self.UMAX)
        return server

    def assign_task_to_server(self, task_tick) -> None:
        """Assign a task to a server.

        Assign a task to an existent server or create a
        new server and assign the task to the new instance.
        """
        if not self.verify_available_server_existence():
            server = self.create_a_server()
            server.connect(User(task_tick))
            self.servers.append()
        for server in self.servers:
            if server.available():
                server.connect()
