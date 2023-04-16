
import time

###Threading Example

import _thread, threading

class ThreadExample:
    
    def __init__(self):
        self.count = 100
        self.message = "0"

    def firstThread(self):
        for i in range(self.count):
            print("##" + str(i))
      

    def mainThread(self):
        for j in range(self.count):
            print("$$" + str(j))
            time.sleep(.02)
           
    def secondThread(self):
        for k in range(self.count):
            print("**" + str(k))
             
    def timedFunction(self):
        print("                3 seconds is up")
        
inst = ThreadExample()

t = threading.Timer(0.2, inst.timedFunction)
t.start()
##inst.firstThread()
##inst.secondThread()
try:
    _thread.start_new_thread(inst.firstThread,())
except:
   print ("Error: unable to start thread")
try:
    _thread.start_new_thread(inst.secondThread,())
except:
   print ("Error: unable to start thread")
inst.mainThread()
print("We are done")

