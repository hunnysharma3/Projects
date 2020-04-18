import time
from collections import deque
class Scheduler:
    def __init__(self):
        self.ready = deque()
        self.sleeping = [ ]
        self.sequence = 0       
    
    def run(self):
        while self.ready or self.sleeping:
	        if not self.ready:
            	deadline, _,func = heapq.heappop(self.sleeping)
                delta = deadline - time.time()
                
                if delta < 0:
                   	delta = 0
                time.sleep(delta)
                self.ready.append(func)
         
            func = self.ready.popleft()
	        func()

    def call_soon(self,func):
        self.ready.append(func)
    
    def call_later(self, delay, func):
        deadline = time.time() + delay
        self.sequence += 1
        heapq.heappush(self.sleeping, (deadline, self.sequence, func) )    
  
sched = Scheduler()

def countdown(n):
    if n > 0:
        print ('Down',n)
        #time.sleep(4)
        sched.call_later(4, lambda: countdown(n-1))
         

def countup(stop, x=0):
    
    if x < stop:
        print ('Up',x)
        #time.sleep(1);
        sched.call_later(1, lambda: countup(stop, x+1))

sched.call_soon(lambda: countdown(5))
sched.call_soon(lambda: countup(5))
sched.run()


