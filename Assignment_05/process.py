class Process:
    
    def __init__(self) -> None:
        self.id = 0
        self.priority = 0
        self.at = 0
        self.bt = 0
        self.ct = 0
        self.tat = 0
        self.wt = 0
        self.remaining_burst_time = 0

    def __str__( self ) -> str:
        return f"process: {self.id} AT = {self.at} , BT = {self.bt} , CT = {self.ct} , TAT = {self.tat} , WT = {self.wt} , PRIORITY = {self.priority}"  
    

