'''
Threading excels in I/O-bound tasks, while multiprocessing is better suited for CPU-bound tasks.

I/O-bound vs CPU-bound:

    CPU-bound task → needs lots of processing power (e.g., big calculations).
        - GIL blocks true parallel execution in threads.
    I/O-bound task → spends most time waiting (e.g., network, file, DB).
        - While one thread is waiting, the GIL is released.
        - Another thread can run in the meantime.
'''

import threading
import requests
import time

def download(url):
    print(f"Starting downloading from {url}")
    resp = requests.get(url)
    print(f"Finished downloading from {url}, size: {len(resp.content)} bytes")
    
urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

start = time.time()
threads = []

for url in urls:
    t = threading.Thread(target=download, args=(url, ))
    t.start()
    threads.append(t)
    
for t in threads:
    t.join()
    
end = time.time()

print(f"All downloads are done in {end - start: .2f} seconds")