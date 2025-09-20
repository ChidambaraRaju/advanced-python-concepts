"""
-In multiprocessing, each process has its own separate memory space (unlike threads).
That means variables can't be directly shared.
- To communicate safely between processes, Python provides Queue,
which works like a pipe with thread/process-safe read/write operations.
"""

from multiprocessing import Process, Queue

def prepare_chai(queue):
    queue.put("Masala chai is ready")



if __name__ == '__main__':
    queue = Queue()

    p = Process(target=prepare_chai, args=(queue,))
    p.start()
    p.join()
    print(queue.get())