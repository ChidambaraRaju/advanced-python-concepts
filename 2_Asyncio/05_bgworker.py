import asyncio
import threading
import time

def background_worker(): # runs in a separate thread
    while True:
        time.sleep(1)
        print(f"Logging the system health 🕰️") 

async def fetch_orders(): # runs in the main thread
    await asyncio.sleep(3)
    print("🎁 order fetched")


threading.Thread(target=background_worker, daemon=True).start() # daemon=True means the thread will exit when the main program exits

asyncio.run(fetch_orders())