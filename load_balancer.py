"""

Constant value for tick cost COST_PER_TICK = 1.00
tick -> basic time unit
ttask -> ticks for a task conclusion
umax -> simultaneous user per server


"""


class Task:
    def __init__(self, ticks_to_conclusion):
        self.ticks_to_conclusion = ticks_to_conclusion

    def execute(self):
        self.ticks_to_conclusion -= 1

    def complete(self):
        return not self.ticks_to_conclusion
