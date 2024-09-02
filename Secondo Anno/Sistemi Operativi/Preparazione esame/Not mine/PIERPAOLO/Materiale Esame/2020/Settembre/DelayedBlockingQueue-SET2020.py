#!/usr/bin/python3

from threading import RLock,Thread,Condition
import time
import random

'''
    Classe Thread che aiuta a inserire elementi in ritardo.
'''

class Putter(Thread):
    
    def __init__(self,dcoda,e,d):
        super().__init__()
        self.dcoda = dcoda
        self.e = e
        self.d = d
        
    def run(self):
        self.dcoda.putRitardato(self.e,self.d)


class DelayedBlockingQueue:

    # 
    # 	 * Costruisce una DelayedBlockingQueue
    # 	 * 
    # 	 * @param d
    # 	 *            Ritardo iniziale di default
    # 	 * @param size
    # 	 *            Dimensione massima della blocking queue
    # 	 
    def __init__(self, d, size : int):
        # 
        #   Lock per la gestione dei campi interni alla coda
        #      
        self.wlock = RLock()
        #   
        #   Condizioni di attesa
        # 
        self.full = Condition(self.wlock)
        self.empty = Condition(self.wlock)
        self.sleepCondition = Condition(self.wlock)
    
        # 
        #   Coda degli elementi con ritardo scaduto e pronti al prelievo
        #      
        self.coda = []
    
        # 
        #   Taglia massima di 'coda'
        #      
        self.maxSize = size    
        # 
        #   Collezione degli elementi non ancora scaduti e abbinati insieme al
        #   tempo in cui scadranno
        #      
        self.scadenze = {}    
        # 
        #   Ritardo di default
        #      
        self.delay = d


    # 
    # 	 * Restituisce il ritardo di default
    # 	 * 
    # 	 * @return il ritardo di default in millisecondi
    # 	 
    def getDelay(self):
        with self.wlock:
            return self.delay

    # 
    # 	 * Imposta il ritardo di default
    # 	 * 
    # 	 * @param d
    # 	 *            il nuovo valore del ritardo di default, in millisecondi
    # 	 
    def setDelay(self, d):
        with self.wlock:
            self.delay = d

    # 
    # 	 * Inserisce un elemento nella DelayedBlockingQueue, con ritardo di default.
    # 	 * 
    # 	 * @param e
    # 	 *            elemento di tipo T da inserire
    # 	 
    def put(self, e, d = None):
        with self.wlock:
            if d == None:
                d = self.getDelay()
            Putter(self,e,d).start()

    # 
    # 	 * Inserimento di un elemento nella DelayedBlockingQueue, con ritardo a
    # 	 * piacere. L'elemento viene inserito in differita sfruttando un thread che
    # 	 * dorme per d millisecondi e inserisce in coda allo scadere del tempo. Nel
    # 	 * frattempo si tiene traccia del momento della scadenza per poter
    # 	 * implementare il metodo poll()
    # 	 * 
    # 	 * @param e
    # 	 *            elemento di tipo T da inserire
    # 	 * @param d
    # 	 *            ritardo passato il quale l'elemento sara' disponibile, in
    # 	 *            millisecondi
    # 	 
    def putRitardato(self,e,d):
                 
        with self.wlock:
            while len(self.coda)+len(self.scadenze) == self.maxSize:
                self.full.wait()
            quandoScade = time.time() + d
            self.scadenze[e] = quandoScade

            #
            #  Per evitare eventuali risvegli spuri, usiamo un ciclo di controllo
            #
            while time.time() < quandoScade:
                self.sleepCondition.wait(d)
                d = time.time() - quandoScade
            

            del self.scadenze[e]
            self.veraPut(e)

    
 
    # 
    # 	 * inserisce effettivamente un elemento in coda. Usato quando scade il tempo
    # 	 * di attesa
    # 	 * 
    # 	 * @param e elemento da inserire
    # 	 
    def veraPut(self, e):
        self.coda.insert(0,e)
        self.empty.notify_all()

    # 
    # 	 * Prelievo da coda. Coincide sostanzialmente con il normalissimo codice di
    # 	 * prelievo da una blockingqueue standard
    # 	 * 
     # 	 
    def take(self):
        with self.wlock:
            while len(self.coda) == 0:
                self.empty.wait()
            self.full.notify_all()
            return self.coda.pop()

    # 
    # 	 * Calcola il tempo mancante come la piu' imminente delle scadenze meno il
    # 	 * tempo corrente
    # 	 * 
    # 	 
    def poll(self):
        with self.wlock:
            if len(self.coda) > 0:
                return 0
            elif len(self.scadenze) > 0:
                tempoMancante = self.scadenze[min(self.scadenze, key=lambda x: self.scadenze[x] )] - time.time()
                
                # 
                #  Per eliminare le situazioni in cui c'e' un elemento in
                #  scadenza imminente (o gia' avvenuta) tale per cui
                #  tempoMancante <= 0, ma ancora il thread che fa l'inserimento
                #  non ha potuto inserire.
                # 
                return tempoMancante if tempoMancante > 0 else 0
            else:
                return -1
            
            
    def minScadenza(self):
        #
        # Metodo che illustra a cosa equivale:
        # self.scadenze[min(self.scadenze, key=lambda x: self.scadenze[x] )]
        # non realmente usato.
        #
        min = None
        for key in self.scadenze:
            if min == None or self.scadenze[key] < min:
                min == self.scadenze[key]
        return min
            
    def show(self):
        
        with self.wlock:
            
            print ("MIN:{0:.2f} ".format(self.poll()),end='')

            for e in self.coda:
                print ("{}:0 ".format(e), end='')
            
            for e in self.scadenze:
                print("{0:}:{1:.3f} ".format(e,self.scadenze[e]-time.time()),end='')
            
            print()
'''
    Classi Consumer e Producer di test
'''
class Consumer(Thread): 
    
    
    def __init__(self,buffer):
        self.queue = buffer
        Thread.__init__(self)

    def run(self):
        while True:
            time.sleep(random.random()*2)
            self.queue.take()
            self.queue.show()


class Producer(Thread):

    counter = 0

    def __init__(self,buffer):
        self.queue = buffer
        Thread.__init__(self)

    def run(self): 
        while True:
            time.sleep(random.random() * 2)
            Producer.counter +=1
            self.queue.put("E-{}.{}".format(self.name,Producer.counter),random.random()*5)
            self.queue.show()
#
#  Main
#
buffer = DelayedBlockingQueue(1,10)

producers = [Producer(buffer) for x in range(3)]
consumers = [Consumer(buffer) for x in range(10)]

for p in producers:
    p.start()

for c in consumers:
    c.start()

print ("Started")