import random

no_of_chunks = 10
programs = 5

program_chunks= []
memory = []
total_memory = 0

last_inserted_chunk = 0

def best_fit(required_memory):
    minMemoryIndex = -1
    minMemoryChunkSize = float('inf')

    for i in range(len(memory)):
        
        if (memory[i][1] < minMemoryChunkSize and memory[i][2]) and (memory[i][1] >= required_memory):
            minMemoryChunkSize = memory[i][1]
            minMemoryIndex = i

    
    memory[minMemoryIndex][1] = memory[minMemoryIndex][0] - required_memory
    memory[minMemoryIndex][2] = False
    last_inserted_chunk = minMemoryIndex

    print(f"Inserted the chunk successfuly at {last_inserted_chunk}")



def worst_fit(required_memory):
    maxMemoryIndex = -1
    maxMemoryChunkSize = float('-inf')
    for i in range(len(memory)):
        
        if (memory[i][1] > maxMemoryChunkSize and memory[i][2]) and (memory[i][1] >= required_memory):
            maxMemoryChunkSize = memory[i][1]
            maxMemoryIndex = i

    
    memory[maxMemoryIndex][1] = memory[maxMemoryIndex][0] - required_memory
    memory[maxMemoryIndex][2] = False
    last_inserted_chunk = maxMemoryIndex

    print(f"Inserted the chunk successfuly at {last_inserted_chunk}")


def first_fit(required_memory):
    pass

def next_fit(required_memory):
    pass
def main():
    #initialize memory
    global last_inserted_chunk, total_memory, memory, programs, no_of_chunks

    #initialize memory
    for _ in range(no_of_chunks):
        block_size = random.randint(10,100)
        remaining_size = block_size
        is_Free = True

        memory.append([block_size, remaining_size, is_Free])
        total_memory+=block_size

    #initialize programs
    for _ in range(programs):
        program_size = random.randint(10,60)
        program_chunks.append(program_size)

    print("\nPROGRAMS")
    for prog in program_chunks:
        print(prog)

    for prog in program_chunks:
        print("\nMEMORY")
        for mem in memory:
            print(mem)

        print(f"\nAllocate memory to {prog}")

        choice = int(input("What do you want to do?\n1.Best fit\n2.First Fit\n3.Worst Fit\n4.Next Fit\n>>> "))

        if choice == 1:
            best_fit(required_memory=prog)
        
        elif choice == 2:
            first_fit(required_memory=prog)

        elif choice == 3:
            worst_fit(required_memory=prog)

        elif choice == 4:
            next_fit(required_memory=prog)

        

    


if __name__ == '__main__':
    main()

