import asyncio
import time # blocking call
from concurrent.futures import ThreadPoolExecutor # run blocking functions in separate threads.

def check_stock(item):
    print(f"Checking {item} in store...")
    time.sleep(3) # Blocking operation
    return f"{item} stock: 42"

async def main():
    loop = asyncio.get_running_loop() # Gets the currently running event loop.
    with ThreadPoolExecutor() as pool: # Creates a pool of threads
        result = await loop.run_in_executor(pool, check_stock, "Masala chai") # Runs the blocking function in a separate thread
        print(result)

asyncio.run(main()) # Starts the asyncio event loop and runs the main coroutine.