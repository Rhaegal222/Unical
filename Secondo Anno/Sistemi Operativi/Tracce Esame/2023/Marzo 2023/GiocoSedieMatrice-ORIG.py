from threading import Thread, Lock, current_thread
from time import sleep
from random import random, randrange

'''
    Versione del gioco delle sedie con una matrice di posti. 
   
    Rispetto all'esempio che viene fatto tradizionalmente in ogni edizione del corso:
     - i partecipanti lavorano su una matrice di sedie anziche su una lista, al fine di simulare la prenotazione dei posti di una sala con un numero di posti disposti in griglia quadrata (LATOSALA = numero file).
     - la stampa tiene conto della presenza di una matrice quadrata;
     - il PartecipanteSafe sceglie un posto casuale;
     - Vi ho lasciato il codice della soluzione A e della soluzione B per come fatto a lezione, per ricordarvi le cose che NON SI DEVONO fare, ma la traccia di esame sarà basata sulla soluzione C.

    Vi ricordo come sono fatte le tre possibili soluzioni: soluzione A senza lock (sbagliata), soluzione B con i lock ma usati male (sbagliata), soluzione C con i lock usati bene (corretta)

    Soluzione A:
        - Fatta creando un array di PostoUnsafe e usando come thread PartecipanteUnsafe

        In questa soluzione non viene usata alcuna forma di locking. Facendo girare il gioco più volte, riscontrerete che a volte tutti i Partecipanti riescono a sedersi, 
        poichè qualcuno si siede sulla stessa sedia

    Soluzione B:
        - Fatta creando un array di PostoQuasiSafe e usando come thread PartecipanteUnSafe

        Questa soluzione ha lo stesso problema della soluzione A. 
        Anche se libero() e set() sono, prese singolarmente, thread-safe, queste vengono chiamate in due tempi distinti (PRIMO TEMPO: chiamata a libero; SECONDO TEMPO: chiamata a set() ), acquisendo e rilasciando il lock entrambe le volte. 
        In mezzo ai due tempi, eventuali altri partecipanti avranno la possibilità di acquisire il lock su self.posti[i] e modificarne lo stato. Noi non vogliamo questo. E' una race condition.

    Soluzione C:
        - Fatta usando un array di PostoSafe e usando come thread PartecipanteSafe

'''

class PostoUnsafe:
    def __init__(self):
        self.occupato = False

    def libero(self):
        return not self.occupato

    def set(self, v):
        self.occupato = v


class PostoQuasiSafe(PostoUnsafe):
    def __init__(self):
        super().__init__()
        self.lock = Lock()

    def libero(self):
        '''
        Il blocco "with self.lock" è equivalente a circondare tutte le istruzioni in esso contenute con self.lock.acquire() e self.lock.release()
        Notate che questo costrutto è molto comodo in presenza di return, poichè self.lock.release() verrà eseguita DOPO la return, cosa che normalmente
        non sarebbe possibile (return normalmente è l'ultima istruzione di una funzione)
        '''
        with self.lock:
            return super().libero()

    def set(self, v):
        self.lock.acquire()
        super().set(v)
        self.lock.release()


class PostoSafe(PostoQuasiSafe):
    def __init__(self):
        super().__init__()

    def testaEoccupa(self):
        with self.lock:
            if self.occupato:
                return False
            else:
                self.occupato = True
                return True


class Display(Thread):

    def __init__(self, posti):
        super().__init__()
        self.posti = posti

    def run(self):
        while True:
            sleep(1)
            print(f"+{'-' * len(self.posti[0]) * 2}+")
            for i in range(len(self.posti)):
                row = "|"
                for j in range(len(self.posti[0])):
                    if self.posti[i][j].libero():
                        row += ". "
                    else:
                        row += "o "
                row += "|"
                print(row)
            print(f"+{'-' * len(self.posti[0]) * 2}+")


class PartecipanteUnsafe(Thread):
    def __init__(self, posti):
        super().__init__()
        self.posti = posti

    def run(self):
        sleep(randrange(5))
        for i in range(len(self.posti)):
            for j in range(len(self.posti[0])):
                if self.posti[i][j].libero():
                    self.posti[i][j].set(True)
                    print(f"Sono il Thread {current_thread().name}. Occupo il posto {i},{j}")
                    return

        print(f"Sono il Thread {current_thread().name}. HO PERSO")

class PartecipanteSafe(Thread):
    def __init__(self, posti):
        super().__init__()
        self.posti = posti

    def run(self):
        tentativi = set()
        while len(tentativi) < len(self.posti) * len(self.posti[0]):
            sleep(randrange(1))
            i = randrange(len(self.posti))
            j = randrange(len(self.posti[0]))
            if (i, j) not in tentativi and self.posti[i][j].testaEoccupa():
                print(f"Sono il Thread {current_thread().name}. Occupo il posto ({i},{j})")
                return
            tentativi.add((i, j))

        print(f"Sono il Thread {current_thread().name}. HO PERSO")

LATOSALA = 10
posti = [[PostoSafe() for j in range(LATOSALA)] for i in range(LATOSALA)]

lg = Display(posti)
lg.start()

for i in range(LATOSALA*LATOSALA+5):
    # t = PartecipanteUnsafe(posti)
    t = PartecipanteSafe(posti)
    t.setName(f"Spettatore-{i}")
    t.start()