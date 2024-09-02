from threading import * 

class Sedia():
    def __init__(self):
        self.lock = Lock()      # Il lock bisogna dichiararlo SEMPRE nella risorsa a cui dobbiamo accedere
        self.occupata = False

class Persona(Thread):          # La classe che dovrà essere il thread sarà quella che dovrà effettuare l'accesso alla risorsa (ovvero le sedie)
    def __init__(self,id,sedie):
        super().__init__()
        self.id = id
        self.sedie = sedie

    def run(self):
        for i in range(len(self.sedie)):
            seduto = False
            self.sedie[i].lock.acquire()                 # Bisogna lockare la risorsa prima che venghi realmente occupata, così dopo possiamo controllare se è occupata o meno
            if not self.sedie[i].occupata:               # Serve per evitare la starvation (quando più thread aspettano la stessa risorsa a vuoto)            
                self.sedie[i].occupata = True
                print(f"Sono il thread {self.id}, e sono sulla sedia {i}")
                seduto = True
                self.sedie[i].lock.release()              # Bisogna SEMPRE rilasciare la risorsa dopo averla utilizzata, altrimenti si va in deadlock perchè risulterà sempre occupata
                break
            self.sedie[i].lock.release()
            if seduto: break

        if not seduto:
            print(f"Sono il thread {self.id} e ho perso")

nsedie = 10
lista_sedie = [Sedia() for i in range(nsedie)]
lista_partecipanti = [Persona(i, lista_sedie) for i in range(nsedie + 1)]

for i in range(nsedie + 1):
    lista_partecipanti[i].start()  # Per sfruttare un thread bisogna usare start() e non run(), perchè usando il run() eseguirà sempre un thread per volta
