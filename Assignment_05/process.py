class Process:

    def __init__(self) -> None:
        self.id = 0
        self.at = 0
        self.bt = 0
        self.ct = 0
        self.tat = 0
        self.wt = 0
        self.remaining_burst_time = self.bt
        self.priority = 0

    def __str__(self) -> str:
        return f"{self.id}\t{self.at}\t\t{self.bt}\t\t{self.ct}\t\t{self.wt}\t\t{self.tat}\t{self.priority}"