from server import Server
from user import User


class LoadBalancer:
    def __init__(self, ttask: int, umax: int):
        self.TTASK = ttask
        self.UMAX = umax
        self.servers = list()
        self.total = int()
        self.total_users = int()

    def calculate_total(self) -> int:
        """"Calculate the total cost of all servers.

        Calculate the total cost of all servers on servers
        attributes.
        """
        total = int()
        for server in self.servers:
            total = server.calculate_total_per_tick() + total
        self.total = total
        return total

    def calculate_user(self) -> int:
        total_users = int()

        for server in self.servers:
            total_users += server.total_users()

        self.total_users = total_users
        return total_users

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

    def assign_task_to_server(self, task_tick: int) -> None:
        """Assign a task to a server.

        Assign a task to an existent server or create a
        new server and assign the task to the new instance.
        """
        if not self.verify_available_server_existence():
            server = self.create_a_server()
            server.connect(User(task_tick))
            self.servers.append(server)
        for server in self.servers:
            if server.available():
                server.connect(User(task_tick))

    def execute_users(self):
        for server in self.servers:
            server.execute_tasks()

    def disconnect_users(self):
        for server in self.servers:
            server.disconnect()