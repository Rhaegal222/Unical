from threading import Condition, Lock


class BlockingQueue:

    def __init__(self,dim):
        self.lock = Lock()
        self.full_condition = Condition(self.lock)
        self.empty_condition = Condition(self.lock)
        self.ins = 0
        self.out = 0
        self.slotPieni = 0
        self.dim = dim
        self.thebuffer = [None] * dim
        
    def put(self,c):
        self.lock.acquire()
        
        while self.slotPieni == len(self.thebuffer):
            self.full_condition.wait()
        
        self.thebuffer[self.ins] = c
        self.ins = (self.ins + 1) % len(self.thebuffer)
        
        self.empty_condition.notifyAll()
        
        self.slotPieni += 1
        self.lock.release()

    def show(self):
        
        self.lock.acquire()
        val = [None] * self.dim;
        
        for i in range(0,self.slotPieni):
            val[(self.out + i) % len(self.thebuffer)] = '*'
        
        for i in range(0,len(self.thebuffer) - self.slotPieni):
            val[(self.ins + i) % len(self.thebuffer)] = '-'
        
        print("In: %d Out: %d C: %d" % (self.ins,self.out,self.slotPieni))
        print("".join(val))
        self.lock.release()


    def get(self): 

        self.lock.acquire()
        try:
            while self.slotPieni == 0:
                self.empty_condition.wait()
    
            returnValue = self.thebuffer[self.out]
            self.out = (self.out + 1) % len(self.thebuffer)
            
            self.full_condition.notifyAll()
            
            self.slotPieni -= 1
            return returnValue
        finally:
            self.lock.release()
   
