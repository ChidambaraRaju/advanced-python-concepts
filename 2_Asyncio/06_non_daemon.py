import threading
import time

def monitor_tea_temp():
    while True:
        print(f"Monitoring tea temperature...")
        time.sleep(2)

t = threading.Thread(target=monitor_tea_temp) # non-daemon thread, will keep the program running
# t = threading.Thread(target=monitor_tea_temp, daemon=True) # daemon thread, will exit when main program exits
t.start()

print("Main program done")