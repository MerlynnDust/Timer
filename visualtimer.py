import time
import console

class customtimer():
    
    def __init__(self):
        print("initializing timer object")
        time.sleep(1)
        console.clear()
        
    def asktimer(self):
        self.timeramount = int(input("how many minutes do you want the timer for? ")) * 60
        console.clear()
    
    def runtimer(self):
        for minutes in reversed(range(self.timeramount)):
            print(minutes)
            time.sleep(1)
            console.clear()
            
mytimer = customtimer()
mytimer.asktimer()
mytimer.runtimer()
