# First Come First Serve
from collections import deque
from process import Process

def fcfs_scheduling(process_list: list[Process]):
    no_of_processes = len(process_list)
    completed_processes = 0

    ready_list = deque()
    shceduled_list = []

    curr_proc: Process = None
    time = 0

    while no_of_processes != completed_processes:

        for proc in process_list:
            if proc.at == time:
                print(f"At time {time} Process {proc.id} ready")
                ready_list.append(proc)

        # give attention
        if curr_proc is None and len(ready_list) > 0:
            curr_proc = ready_list.popleft()

        # run
        if curr_proc is not None:
            curr_proc.remaining_burst_time -= 1

        if curr_proc is not None and  curr_proc.remaining_burst_time == 0:
            
            curr_proc.ct = time + 1
            curr_proc.tat =curr_proc.ct - curr_proc.at
            curr_proc.wt =curr_proc.tat - curr_proc.bt
            shceduled_list.append(curr_proc)
            curr_proc = None

            

            completed_processes += 1
            

        time += 1
    
    for proc in shceduled_list:
        print(proc)





def main():

    # no_of_processes = int(input("Enter no. of Processes : "))
    # arrival_times = list(map(int, input("Enter Arrival times of Processes: ").split(" ")))
    # burst_times = list(map(int, input("Enter Burst times of Processes : ").split(" ")))

    no_of_processes = 6
    arrival_times = [0, 1, 1, 1, 2, 3]
    burst_times = [9, 3, 2, 4, 3, 2]

    print("Number of Processes : ", no_of_processes)
    print("Arrival Times : ", arrival_times)
    print("Burst Times : ", burst_times)

    process_list = []

    for i in range(no_of_processes):
        process = Process()
        process.id = i+1
        process.at = arrival_times[i]
        process.bt = burst_times[i]
        process.remaining_burst_time = burst_times[i]

        process_list.append(process)

    fcfs_scheduling(process_list)


if __name__ == "__main__":
    main()


# input
# 6
# 0 1 1 1 2 3
# 9 3 2 4 3 2