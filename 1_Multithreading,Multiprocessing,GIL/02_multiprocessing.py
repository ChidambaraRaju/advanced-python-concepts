'''
- Multiprocessing means running multiple tasks in seperate processes
- Each process has its own memory space and runs independently
'''

from multiprocessing import Process
import time

def brew_chai(name):
    print(f"Start of {name} chai brewing")
    time.sleep(3)
    print(f"ENd of {name} chai brewing")
    
    
if __name__ == "__main__":
    chai_makers = [
        Process(target=brew_chai, args=(f"Chai Maker #{i+1}",))
        for i in range(3)
    ]
    
    for p in chai_makers:
        p.start() # Start all the process
        
    for p in chai_makers:
        p.join() # Wait until all the process are done
        
    print("All Chai Served")
        
    