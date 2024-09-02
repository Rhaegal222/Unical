
#RISORSA PONTE
from queue import Queue
from time import sleep
from random import randint
from threading import Condition, RLock, Thread


class Ponte:
    def __init__(self,N,dir):
        self.capienza=N
        self.occupati=0
        self.lock = RLock() 
        self.condition = Condition(self.lock)
        self.currentDir=dir
        self.waiting_mare = 0
        self.waiting_montagna = 0
        self.queue = Queue()  # Aggiungi una coda per tracciare l'ordine di arrivo

    
    def mareToMontagna(self,name):
         with self.lock:
            self.waiting_mare+=1
            self.queue.put(name)  # Aggiungi il nome del thread alla coda quando arriva
            print(f"il thread {name} ha provato ad attraversare dal mare verso la montagna", flush=True)
            while self.currentDir == 1 or (self.currentDir == -1 and self.waiting_montagna > self.waiting_mare) or self.occupati >= self.capienza or self.queue.queue[0] != name: #se il ponte è occupato e la direzione è diversa da quella del thread
                print(f"il thread {name} ha trovato il ponte occupato e si mette in attesa dal lato mare", flush=True)
                self.condition.wait()
            self.occupati += 1
            self.waiting_mare  -= 1
            self.currentDir = 0
            print(f"il thread {name} sta attraversando il ponte dal mare verso la montagna", flush=True)
            self.queue.get()  # Rimuovi il thread dalla coda quando inizia a attraversare il ponte
            
            sleep(randint(1, 5))  # Tempo di attraversamento variabile tra 1 e 5 secondi

            self.occupati -= 1
            
            print(f"Il thread {name} ha lasciato il ponte", flush=True)
            if self.occupati == 0 and self.waiting_montagna > 0:
                # Se il ponte è vuoto, possiamo cambiare direzione
                self.currentDir = 1
                self.condition.notify_all()


    def montagnaToMare(self,name):
        with self.lock:
            self.queue.put(name)  # Aggiungi il nome del thread alla coda quando arriva
            self.waiting_montagna += 1
            print(f"il thread {name} ha provato ad attraversare dalla montagna verso il mare", flush=True)
            while self.currentDir == 0 or (self.currentDir == -1 and self.waiting_mare > self.waiting_montagna) or self.occupati >= self.capienza or self.queue.queue[0] != name:
                print(f"il thread {name} ha trovato il ponte occupato e si mette in attesa dal lato montagna", flush=True)
                self.condition.wait()
            self.waiting_montagna -= 1
            self.occupati+=1
            self.currentDir=1
            print(f"il thread {name} sta attraversando il ponte dalla montagna verso il mare", flush=True)
            self.queue.get()  # Rimuovi il thread dalla coda quando inizia a attraversare il ponte

            sleep(randint(1, 5))  # Tempo di attraversamento variabile tra 1 e 5 secondi

            self.occupati -= 1
            print(f"Il thread {name} ha lasciato il ponte", flush=True)
            if self.occupati == 0 and self.waiting_mare > 0:
                # Se il ponte è vuoto, possiamo cambiare direzione
                self.currentDir = 0 
                self.condition.notify_all()



#THREAD TURISTA
class Turista(Thread):
    cont=0
    def __init__(self,dir,ponte):
        super().__init__()
        self.ponte=ponte
        self.dir=dir #dir=0, dal mare alla montagna, dir=1 da montagna al mare
    def run(self):
        #while True:
            if self.dir == 0:
                self.ponte.mareToMontagna(self.name)
            elif self.dir == 1:
                self.ponte.montagnaToMare(self.name)

            sleep(randint(1, 3))  # Pausa tra i tentativi di attraversamento

                 

class main:
    def __init__(self):
        ponte=Ponte(5,-1)
        for i in range(10):
            t=Turista(randint(0,1),ponte)
            t.start()

if __name__ == "__main__":
    main()