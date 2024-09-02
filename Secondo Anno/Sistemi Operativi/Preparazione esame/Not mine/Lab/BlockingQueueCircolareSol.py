import random, time
from threading import Thread, Lock, Condition


class BlockingQueue:

    def __init__(self,dim):
        self.lock = Lock()
        self.full_condition = Condition(self.lock)
        self.empty_condition = Condition(self.lock)
        self.ins = 0 #indice di scrittura
        self.out = 0 #indice di lettura
        self.slotPieni = 0
        self.dim = dim
        self.thebuffer = [None] * dim
        
    def put(self,c): # put il carattere c nel buffer
        self.lock.acquire()
        
        while self.slotPieni == len(self.thebuffer):
            self.full_condition.wait()
        
        self.thebuffer[self.ins] = c
        self.ins = (self.ins + 1) % len(self.thebuffer)
        
        self.empty_condition.notifyAll()
        
        self.slotPieni += 1
        self.lock.release()

    def show(self): # mostra il contenuto del buffer
        
        self.lock.acquire()
        val = [None] * self.dim;
        
        for i in range(0,self.slotPieni):
            val[(self.out + i) % len(self.thebuffer)] = '*' # '*' indica che c'è un carattere
        
        for i in range(0,len(self.thebuffer) - self.slotPieni):
            val[(self.ins + i) % len(self.thebuffer)] = '-' # '-' indica che non c'è un carattere
        
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

class Consumer(Thread): 
    
    def __init__(self,buffer):
        self.queue = buffer
        Thread.__init__(self)

    def run(self):
        while True:
            time.sleep(random.random()*2)
            self.queue.get()
            self.queue.show()


class Producer(Thread):

    def __init__(self,buffer):
        self.queue = buffer
        Thread.__init__(self)

    def run(self): 
        while True:
            time.sleep(random.random() * 2)
            self.queue.put(self.name)
            self.queue.show()
#
#  Main
#
if __name__ == "__main__":

    buffer = BlockingQueue(10)

    producers = [Producer(buffer) for x in range(5)]
    consumers = [Consumer(buffer) for x in range(3)]

    for p in producers:
        p.start()

    for c in consumers:
        c.start()
