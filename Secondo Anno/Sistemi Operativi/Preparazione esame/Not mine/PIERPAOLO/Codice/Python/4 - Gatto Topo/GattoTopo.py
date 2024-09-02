from random import randint
from threading import Thread, Lock
from time import sleep


class Striscia:
    LUNG = 20

    def __init__(self):
        self.striscia = []
        self.fine = False   #   Indica se il gatto ha preso il topo
        self.dirGatto = 1   #   -1 quando tocca il bordo una volta

        self.topo = randint(0, self.LUNG-1) #   Posizione iniziale casuale Topo
        self.gatto = randint(0, self.LUNG-1) #  Posizione iniziale casuale Gatto
        while(self.gatto==self.topo):   #   Rigenera la posizione del topo fino a quando self.gatto e self.topo non saranno diversi
            self.gatto = randint(0, self.LUNG-1) 

        for i in range(self.LUNG):
            self.striscia.append(' ')
        self.striscia[self.topo] = '.'
        self.striscia[self.gatto] = '*'

        self.lock = Lock() #    Dichiarazione del lock nella risorsa condivisa


    def printStriscia(self):
        self.lock.acquire() #   Il lock viene aquisito prima che un thread effettui una modifica sulle risorse condivise
        try:
            print("|%s|" % ''.join(self.striscia))
            return self.fine
        finally: #  Il finally viene eseguito a prescindere da un eventuale exception
            self.lock.release()

    def muoviGatto(self):
        self.lock.acquire()
        try:
            if self.fine: # Il gatto ha già preso il topo
                return True #   Il thread può terminare

            self.striscia[self.gatto] = ' ' #   Ripristina la cella occupata dal gatto
            self.gatto += self.dirGatto #   Sposta il gatto

            if self.gatto > self.LUNG-1 or self.gatto < 0: #    Gatto out of range
                self.dirGatto = -self.dirGatto #    Cambia la direzione di movimento del gatto
                self.gatto += 2 * self.dirGatto #   Sposta il gatto

            if self.gatto == self.topo: #   Il gatto prende il topo
                self.fine = True    #   La variabile fine viene settata a true per ritornare TRUE in ogni Thread
                self.striscia[self.gatto] = '@' #   Gatto e topo sono nella stessa cella
                return True #   Il thread può terminare

            self.striscia[self.gatto] = '*' #   Modifica la cella occupata attualmente dal gatto
            return False    #   Il gatto non ha ancora preso il topo, il thread deve continuare
        finally:
            self.lock.release()

    def muoviTopo(self):
        self.lock.acquire()
        try:
            if self.fine: # Il topo è stato già preso dal gatto
                return True #   quindi può dare l'ordine di terminare il Thread

            self.striscia[self.topo] = ' ' #    Ripristina la cella occupata dal topo

            stato = randint(-1, 1) #    Non c'è self perché si tratta di una variabile locale a questa funzione

            if 0 <= self.topo + stato < self.LUNG: #    Se non si verifica out of range
                self.topo = self.topo + stato # Il topo sta fermo o si muove di 1 o torna indietro di 1

            """
            Questo codice è concettualmente sbagliato perchè il topo può andare sulla casella
            occupata dal gatto, gli "salta sopra".
            Solo quando il gatto va nella cella occupata dal topo lo "mangia".

            if self.gatto == self.topo: #il topo è stato preso dal gatto
                self.fine = True
                self.striscia[self.gatto] = '@' #gatto e topo sono nella stessa cella
                return True"""

            self.striscia[self.topo] = '.' #    Aggiorna la posizione del topo
            return False    #   Il topo non è stato catturato quindi non deve dare l'ordine di terminare l'esecuzione del thread
        finally:
            self.lock.release()


class Display(Thread):

    def __init__(self, s):  #   Costruttore del Thread Display
        Thread.__init__(self)   #   Il costruttore di Thread è obbligatorio perchè Display eredita da Thread
        self.striscia = s   #   s è un oggetto della classe Striscia()

    def run(self):  #   Il thread viene avviato
        print("First run Display") 
        while not self.striscia.printStriscia(): #richiama la funzione printStriscia() dichiarata sopra fino a quando non ritorna falso
            sleep(0.10)    #Tempo a scelta dell'utente
            #   L'interprete esegue le istruzioni troppo velocemente per essere visualizzate.
            #   Senza sleep() il programma funzionerebbe comunque in maniera appropriata, ma sarebbe 
            #   illegibile
        print("Il gatto ha preso il topo")  
        


class Gatto(Thread):

    def __init__(self, s):  #   Costruttore del Thread Display
        super().__init__()  #   Il costruttore di Thread è obbligatorio perchè Display eredita da Thread
        self.striscia = s   #   s è un oggetto della classe Striscia()

    def run(self):  #   Il thread viene avviato
        print("First run Gatto")
        while not self.striscia.muoviGatto(): #richiama la funzione muoviGatto()()) striscia dichiarata sopra fino a quando non ritorna falso
            sleep(0.100)    #Tempo a scelta dell'utente
            #   L'interprete esegue le istruzioni troppo velocemente per essere visualizzate.
            #   Senza sleep() il programma funzionerebbe comunque in maniera appropriata, ma sarebbe 
            #   illegibile


class Topo(Thread):

    def __init__(self, s):  #   Costruttore del Thread Display    
        super().__init__()  #   Il costruttore di Thread è obbligatorio perchè Display eredita da Thread
        self.striscia = s   #   s è un oggetto della classe Striscia()

    def run(self):  #   Il thread viene avviato
        print("First run Topo")
        while not self.striscia.muoviTopo(): #richiama la funzione muoviTopo() striscia dichiarata sopra fino a quando non ritorna falso
            sleep(0.100)    #Tempo a scelta dell'utente
            #   L'interprete esegue le istruzioni troppo velocemente per essere visualizzate.
            #   Senza sleep() il programma funzionerebbe comunque in maniera appropriata, ma sarebbe 
            #   illegibile


striscia = Striscia()
jerry = Topo(striscia)
tom = Gatto(striscia)
display = Display(striscia)

print("Created")
print("Started")
display.start()
jerry.start()
tom.start()

sleep(10)
