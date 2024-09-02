import random, time
from threading import Thread, Lock, Condition

'''Blocking queue implementata con il metodo del buffer circolare'''
''' il buffer circolareè una struttura dati utilizzata per l'archiviazione temporanea di dati in cui gli elementi 
    vengono sovrascritti in modo ciclico. gli elementi vengono inseriti alla fine del buffer e, se il buffer è pieno, l'inserimento 
    sovrascrive gli elementi più vecchi presenti all'inizio del buffer (NON IN QUESTO ESERCIZIO). In questo modo, il buffer circolare sembra 
    "avvolgersi" su se stesso, da cui il nome "circolare". Questo meccanismo di sovrascrittura ciclica consente
    di utilizzare un buffer di dimensioni fisse per gestire flussi di dati in entrata di dimensioni variabili.'''
class BlockingQueue:

    def __init__(self,dim):
        self.lock = Lock()
        self.full_condition = Condition(self.lock) #cond buffer pieno
        self.empty_condition = Condition(self.lock) #cond buffer vuoto
        self.ins = 0 #sono indici che indicano head e tail del buffer
        self.out = 0
        self.slotPieni = 0 #spazio occupato nel buffer
        self.dim = dim #dimensione
        self.thebuffer = [None] * dim #riempie di valori nulli il bufferf
        
    def put(self,c):
        self.lock.acquire()
        
        while self.slotPieni == len(self.thebuffer): #se il buffer è piano va in wait : len(self.thebuffer) = dim
            self.full_condition.wait()
        
        self.thebuffer[self.ins] = c #aggiungi elemento c in posizione ins
        self.ins = (self.ins + 1) % len(self.thebuffer) #così se il buffer è pieno, gli elementi venfono sovrascritti (effetto pacman) Esempio: se provo a scrivere su ins+1=11 ma ho un buffer di dim=10 pieno, sovrascrive lelemento in posizione 1
        
        self.empty_condition.notifyAll()
        
        self.slotPieni += 1 #aggiunge elemento al contatore
        self.lock.release()

    def show(self):
        
        self.lock.acquire()
        val = [None] * self.dim; #crea lista grande quanto il buffer
        
        for i in range(0,self.slotPieni):
            val[(self.out + i) % len(self.thebuffer)] = '*' #mette asterischi al posto degli slot pieni
        
        for i in range(0,len(self.thebuffer) - self.slotPieni):
            val[(self.ins + i) % len(self.thebuffer)] = '-' #mette trattini agli spazi vuoti
        
        print("In: %d Out: %d C: %d" % (self.ins,self.out,self.slotPieni)) #stampa ins, out e contatore di slotpieni
        print("".join(val)) #stampa l'array come stringa
        self.lock.release()


    def get(self): 

        self.lock.acquire()
        try:
            while self.slotPieni == 0: #se è vuoto il buffer va in wait
                self.empty_condition.wait()
    
            returnValue = self.thebuffer[self.out] #prende il valore da togliere, il più longevo nel buffer
            self.out = (self.out + 1) % len(self.thebuffer) #aggiorno out
            
            self.full_condition.notifyAll() #notifica tutti i thread in attesa che non fosse pieno il buffer
            
            self.slotPieni -= 1 #aggiorno slotPieni
            return returnValue
        finally: #anche in caso di eccezioni si è sicuri di fare release
            self.lock.release()

class Consumer(Thread): 
    
    def __init__(self,buffer):
        self.queue = buffer
        Thread.__init__(self)

    def run(self):
        while True:
            time.sleep(random.random()*2)
            self.queue.get() #prende un elemento
            self.queue.show() #stampa


class Producer(Thread):

    def __init__(self,buffer):
        self.queue = buffer
        Thread.__init__(self)

    def run(self): 
        while True:
            time.sleep(random.random() * 2)
            self.queue.put(self.name) #mette un nuovo elemento
            self.queue.show() #stampa
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
