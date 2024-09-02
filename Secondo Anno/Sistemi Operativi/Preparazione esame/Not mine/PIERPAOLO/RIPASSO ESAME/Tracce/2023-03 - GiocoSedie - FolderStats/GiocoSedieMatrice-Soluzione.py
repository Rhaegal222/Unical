from threading import Thread, RLock, Lock, current_thread, Condition
from time import sleep
from random import random, randrange


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

    def __init__(self, sala):
        super().__init__()
        self.sala = sala


    def run(self):
        while(self.sala.stampaSala()):
            pass


class PartecipanteUnsafe(Thread):
    def __init__(self, posti, nome):
        super().__init__()
        self.posti = posti
        self.name = nome

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
    def __init__(self, posti, sala, nome):
        super().__init__()
        self.posti = posti
        self.sala = sala
        self.name = nome

    def run(self):
        tentativi = set()
        while len(tentativi) < len(self.posti) * len(self.posti[0]):
            sleep(randrange(1))
            i = randrange(len(self.posti))
            j = randrange(len(self.posti[0]))
            if (i, j) not in tentativi and self.sala.testaEoccupa(i,j):
                print(f"Sono il Thread {current_thread().name}. Occupo il posto ({i},{j})")
                return
            tentativi.add((i, j))
        print(f"Sono il Thread {current_thread().name}. HO PERSO")


class Sala():
    def __init__(self, file):
        self.posti = [[PostoSafe() for j in range(file)] for i in range(file)]
        self.lock = Lock()
        self.condition = Condition(self.lock)
        self.modificato = True
        #booleano che blocca fino a quando ci sono modifiche !!

    def testaEoccupa(self, i, j):
        with self.lock:
            if(self.posti[i][j].testaEoccupa()):
                self.modificato=True
                self.condition.notify()
                return True
            self.modificato=False
            self.condition.notify()
            return False

    def trovaPosto(self):
        with self.lock:
            for i in range (len(self.posti)):
                for j in range(len(self.posti[i])):
                    if(self.testaEoccupa(i,j) ):
                        return i,j
            return -1,-1

    def stampa(self):
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

    def stampaSala(self):
        with self.lock:
            if (self.modificato == True):
                self.stampa()
                self.modificato = False
                self.condition.wait()
                return True
            return False



LATOSALA = 3
NPOSTI = LATOSALA*LATOSALA
NPARTECIPANTI = (LATOSALA*LATOSALA)+3

sala = Sala(LATOSALA)

lg = Display(sala)
lg.start()


for i in range( NPARTECIPANTI ):
    # t = PartecipanteUnsafe(sala.posti, f"Spettatore-{i}")
    t = PartecipanteSafe(sala.posti, sala,f"Spettatore-{i+1}")
    t.start()