class Server:
    def __init__(self, umax: int):
        self.COST_PER_TICK = 1.00

        self.umax = umax
        self.users = list()
        self.total = int()

    def available(self) -> bool:
        return len(self.users) < self.umax

    def connect(self, user) -> None:
        self.users.append(user)

    def total_users(self) -> int:
        return len(self.users)

    def disconnect(self) -> None:
        for user in self.users:
            if user.complete():
                self.users.remove(user)

    def calculate_total_per_tick(self):
        self.total += (self.total_users() * self.COST_PER_TICK)
