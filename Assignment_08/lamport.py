class Process:
    def __init__(self,id):
        self.process_id = id
        self.clock = 0
    
    def perform_local_event(self):
        self.clock += 1
        print(f"Process {self.process_id} performs a local event. Clock = {self.clock}")
    
    def send_message(self,recevier):
        self.clock += 1
        print(f"Process {self.process_id} send a message to {recevier.process_id}. Clock = {self.clock}")
        recevier.receive_message(self.clock)
    

    def receive_message(self,sender_clock):   
        self.clock = max(self.clock,sender_clock) + 1
        print(f"Process {self.process_id} received a message. Clock = {self.clock}")


process_1 = Process(1)
process_2 = Process(2)

process_1.perform_local_event()
process_1.perform_local_event()
process_1.send_message(process_2)