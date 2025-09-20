"""
This program demonstrates safe multi-threaded counter increments using threading.Lock.
With the lock, the final count is correct (1,000,000). Without the lock, race conditions
occur and the result may become inconsistent.
"""

import threading

counter = 0
lock = threading.Lock()

def increament():
    global counter
    for _ in range(100000):
        with lock:
            counter += 1

threads = [threading.Thread(target=increament) for _ in range(10)]
[t.start() for t in threads]
[t.join() for t in threads]

print(f"Final counter: {counter}")