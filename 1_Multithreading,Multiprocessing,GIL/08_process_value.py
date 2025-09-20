"""
multiprocessing.Value allows processes to share a single variable (like an int or float) 
in shared memory, with a built-in lock to prevent race conditions.

Difference: 
- Value → one shared variable across processes. 
- Queue → used for exchanging multiple data/messages between processes.
"""

from multiprocessing import Process, Value

def increment(counter):
    for _ in range(100000):
        with counter.get_lock():
            counter.value += 1


if __name__ == "__main__":
    counter = Value('i', 0)
    processes = [Process(target=increment, args=(counter, )) for _ in range(4)]
    [p.start() for p in processes]
    [p.join() for p in processes]

    print("Final counter value: ",counter.value )