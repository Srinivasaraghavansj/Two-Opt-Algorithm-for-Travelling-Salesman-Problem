"""
This is a program that is made to run the Hillclimbing with different iterations and restart values
"""
#Importing required libraries
import subprocess as sp
from multiprocessing import Process
from multiprocessing import Pool

#Defining parameters to be passed and run to the HillClimbing files
#HillClimbing_no_side.py is side movement restricted version
files = ["HillClimbing.py","HillClimbing_no_side.py"]
max_iters = [100,250,500]
restarts = [10,100,250]

#Function to run the given file with max iters and restarts
def run(file_,max_iter,restart):
    print(f"\n\n\n...\n{file_} {max_iter} {restart}\n{sp.check_output(['time', 'python', str(file_), '120', str(max_iter), str(restart)]).strip().decode()}\n")

#Running the program in different permutations and combinations of the above parameters        
try:
    pool = Pool()
    processes = []
    pool_tasks = []
    for file_ in files:
        for max_iter in max_iters:
            for restart in restarts:
                for i in range(100):
                    pool_tasks.append((file_,max_iter,restart))

'''
I tried using Process first, It was multitasking parallely with 1800 processes, using up all the 16GB of RAM
and using up over 40GB of swap memory. It ran for 3 days, but it didn't finish. So processes was given up.

The better option was Pooling where it feeds the processor with the next task only when a thread of the processor
gets freed up. This time, it ran much much faster and the ram was used not more than 4GB.

'''
    pool.starmap(run,pool_tasks)
    pool.close()
    pool.terminate()
    pool.join()
except KeyboardInterrupt:
    print("Program interrupted manually")

    pool.terminate()

#This file was run from terminal and the outputs were saved to output_1_pooled.txt by using the "&>" command.