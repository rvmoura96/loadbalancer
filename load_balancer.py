from server import Server
from user import User


class LoadBalancer:
    def __init__(self, ttask: int, umax: int):
        self.TTASK = ttask
        self.UMAX = umax
        self.servers = list()
        self.total = int()
        self.total_users = int()

    def calculate_user(self) -> int:
        total_users = int()

        for server in self.servers:
            total_users += server.total_users()

        self.total_users = total_users

        return total_users

    def create_a_server(self) -> Server:
        """"Create a server instance."""
        server = Server(self.UMAX)
        return server

    def assign_task_to_server(self, users) -> None:
        """Assign a task to a server.

        Assign a task to an existent server or create a
        new server and assign the task to the new instance.
        """
        for i in range(users):
            for server in self.servers:
                if server.available():
                    server.connect(User(self.TTASK))
                    break
            else:
                server = self.create_a_server()
                server.connect(User(self.TTASK))
                self.servers.append(server)

    def run_tasks(self):
        for server in self.servers:
            server.execute_tasks()
        self.total += len(self.servers)
        self.servers = [s for s in self.servers if not s.is_empty()]

    def output(self):
        return ", ".join(str(len(s.users)) for s in self.servers)
