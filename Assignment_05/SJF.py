from process import Process
from collections import deque

def sjf_scheduling(process_list: list[Process]):
    time = 0
    ready_list = deque()
    scheduled_list = []
    no_of_processes = len(process_list)
    completed_processes = 0
    curr_proc :Process= None

    while no_of_processes != completed_processes:

        for i in range(len(process_list)):
            if time == process_list[i].at:
                ready_list.append(process_list[i])
                print(f"At time {time} Process {process_list[i].id} is ready")

            

        if (curr_proc is not None) and curr_proc.remaining_burst_time == 0:
            print(f"At time {time} Process {curr_proc.id} completed")
            curr_proc.ct = time
            curr_proc.tat = curr_proc.ct - curr_proc.at
            curr_proc.wt = curr_proc.tat - curr_proc.bt
            scheduled_list.append(curr_proc)
            ready_list.remove(curr_proc)
            curr_proc = None
            completed_processes+=1

        if curr_proc is not None and len(ready_list) > 0:
            min_bt_process = min(ready_list, key=lambda proc: proc.remaining_burst_time)
            if min_bt_process.remaining_burst_time < curr_proc.remaining_burst_time:
                ready_list.remove(min_bt_process)
                ready_list.append(curr_proc)
                curr_proc = min_bt_process

        if curr_proc is None and len(ready_list) > 0:
            curr_proc = min(ready_list, key=lambda proc: proc.bt)
            print(f"At time {time} Process {curr_proc.id} given attention")

        if curr_proc is not None:
            curr_proc.remaining_burst_time = curr_proc.remaining_burst_time - 1

        time+=1

    print(f"ID\tArrival Time\tBurst Time\tCompletion Time\tWaiting Time\tTAT\tPriority")
    for proc in scheduled_list:
        print(proc)

def main():
    # arrival_times = list(map(int, input("Enter arrival times : ").split(" ")))
    # burst_times = list(map(int, input("Enter burst times : ").split(" ")))

    arrival_times = [6, 2, 8, 3, 4]
    burst_times = [2, 5, 1, 0, 4] 

    process_list = []

    for i in range(len(arrival_times)):
        newProcess = Process()
        newProcess.id = i+1
        newProcess.at = arrival_times[i]
        newProcess.bt = burst_times[i]

        newProcess.remaining_burst_time = burst_times[i]
        

        process_list.append(newProcess)

    process_list.sort(key= lambda proc: proc.at)


    print(arrival_times)
    print(burst_times)

    for proc in process_list:
        print(proc)

    sjf_scheduling(process_list)
if __name__ == "__main__":
    main()