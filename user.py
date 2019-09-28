"""

Constant value for tick cost COST_PER_TICK = 1.00
tick -> basic time unit
ttask -> ticks for a task conclusion
umax -> simultaneous user per server


"""


class User:
    def __init__(self, ttask):
        self.ttask = ttask

    def execute(self) -> None:
        self.ttask -= 1

    def complete(self) -> bool:
        return not self.ttask
