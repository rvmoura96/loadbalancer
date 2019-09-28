class Server:
    def __init__(self, umax: int):
        self.COST_PER_TICK = 1.00
        self.umax = umax
        self.users = list()
        self.total = int()

    def available(self) -> bool:
        """Verify the server availability."""
        return len(self.users) < self.umax

    def connect(self, user) -> None:
        """Connect a user/task on server."""
        self.users.append(user)

    def total_users(self) -> int:
        """Return the total user/tasks running."""
        return len(self.users)

    def disconnect(self) -> None:
        """Disconnect all completed users tasks."""
        for user in self.users:
            if user.complete():
                self.users.remove(user)

    def calculate_total_per_tick(self):
        """Calculate the total value per tick run."""
        total = int()
        total += (self.total_users() * self.COST_PER_TICK)
        self.total += total
        return total
