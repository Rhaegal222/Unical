import threading,multiprocessing,time,math

from threading import Lock,Condition,Thread

def eprimo(n):
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(math.sqrt(n)+1),2):
        if n % i == 0:
            return False
    return True

def contaPrimiSequenziale(min,max):

    totale = 0
    for i in range(min,max+1):
    
        if (eprimo(i)):
            totale += 1
    return totale

class Barrier:
    
    def __init__(self,n):
    
        self.soglia = n
        self.threadArrivati = 0
        self.lock = Lock()
        self.condition = Condition(self.lock)


    def wait(self):
        with self.lock:
            self.threadArrivati += 1

            if self.threadArrivati == self.soglia:
                self.condition.notify_all()

            while self.threadArrivati < self.soglia:
                self.condition.wait()

#
#  Metodo non disponibile in CyclicBarrier di Python
#  che consente di incrementare il contatore senza 
#  attendere sulla barriera
#
'''
    def done(self):
        self.lock.acquire()
        self.threadArrivati -= 1
        if self.threadArrivati == 0:
            self.condition.notify_all()
        self.lock.release()
'''



class Macinatore(Thread):

    def __init__(self,nome,min,max,b):

        Thread.__init__(self)
        self.name=nome
        self.min = min
        self.max = max
        self.totale = 0
        self.barriera = b
        self.lock = Lock()
    
    def getTotale(self):
        return self.totale
    
    def run(self):
        self.totale = contaPrimiSequenziale(self.min,self.max)
        with self.lock:
            print(f"Thread {self.name} con range {self.min}-{self.max} ha totale: {self.getTotale()}")
        self.barriera.wait()



def contaPrimiMultiThread(min,max):

    if max < min:
        return 0
   
    threadReali = multiprocessing.cpu_count()
    fetta = (max - min + 1) // threadReali
    while fetta == 0:
        threadReali -= 1
        fetta = (max - min + 1) // threadReali
    print(f"Usero' {threadReali} core")
    
    b = Barrier(threadReali + 1)

    ciucci = []
    
    for i in range(threadReali - 1):
        minI = min + i * fetta
        maxI = min + (i+1)*fetta - 1
        ciucci.append(Macinatore(i,minI, maxI, b))
        ciucci[i].start()
    
    ciucci.append(Macinatore(threadReali - 1,min + (threadReali - 1) * fetta, max, b))
    ciucci[threadReali - 1].start()


    b.wait()


    totale = 0
    for i in range(threadReali):
        totale += ciucci[i].getTotale()
    return totale
    
if __name__ == '__main__':
    
    min = 1000000    # 100_000
    max = 10000000   # 1_000_000
    start = time.time()
    nprimi = contaPrimiMultiThread(min,max)
    elapsed = time.time() - start
    print (f"Primi tra {min} e {max}: {nprimi}")
    print (f"Tempo trascorso: {elapsed} secondi")
