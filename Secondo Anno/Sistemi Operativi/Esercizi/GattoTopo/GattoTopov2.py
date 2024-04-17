from random import randint
from threading import Thread, Lock
from time import sleep

class Striscia:
    LUNG = 50

    def __init__(self):
        self.striscia = [' ' for i in range(self.LUNG)]
        self.fine = False
        self.dirGatto = 1
        self.topo = randint(0, self.LUNG - 1)  # posizione iniziale topo
        self.gatto = randint(0, self.LUNG - 1)  # posizione iniziale gatto
        self.striscia[self.topo] = '.' # posiziono il topo nella striscia
        self.striscia[self.gatto] = '*' # posiziono il gatto nella striscia
        self.lock = Lock()  # dichiarazione del lock nella risorsa condivisa

    def printStriscia(self):
        with self.lock:
            print("|%s|" % ''.join(self.striscia), end='\r')
            return self.fine

    def muoviGatto(self):
        with self.lock:
            if self.fine:  # il gatto ha già preso il topo
                return True

            self.striscia[self.gatto] = ' '  # ripristina la cella occupata dal gatto
            self.gatto += self.dirGatto  # sposta il gatto

            if self.gatto > self.LUNG - 1 or self.gatto < 0:  # gatto out of range
                self.dirGatto = -self.dirGatto  # cambia la direzione di movimento del gatto
                self.gatto += 2 * self.dirGatto  # sposta il gatto

            if self.gatto == self.topo:  # il gatto prende il topo
                self.fine = True
                self.striscia[self.gatto] = '@'  # gatto e topo sono nella stessa cella
                return True

            self.striscia[self.gatto] = '*'  # modifica la cella occupata attualmente dal gatto
            return False

    def muoviTopo(self):
        with self.lock:
            if self.fine:  # il topo è stato già preso dal gatto
                return True

            self.striscia[self.topo] = ' '  # ripristina la cella occupata dal topo

            stato = randint(-1, 1)  # non c'è self perché è locale a questa funzione

            if 0 <= self.topo + stato < self.LUNG:  # se non si verifica out of range
                self.topo = self.topo + stato  # il topo sta fermo o si muove di 1 o torna indietro di 1

            ''' 
            if self.gatto == self.topo:  # il topo è stato preso dal gatto
                self.fine = True
                self.striscia[self.gatto] = '@'  # gatto e topo sono nella stessa cella
                return True* 
            '''

            self.striscia[self.topo] = '.'  # modifica la cella occupata attualmente dal topo
            return False


class Display(Thread):

    def __init__(self, s):
        Thread.__init__(self)
        self.striscia = s

    def run(self):
        print("First run Display")
        while not self.striscia.printStriscia():  # chiama la funzione printStriscia dichiarata sopra fino a quando non ritorna falso
            sleep(0.02)
        print("\nIl topo ha fatto la fine del topo")


class Gatto(Thread):

    def __init__(self, s):
        Thread.__init__(self)
        self.striscia = s

    def run(self):
        print("First run Gatto")
        while not self.striscia.muoviGatto():  # chiama la funzione muoviGatto dichiarata sopra fino a quando non ritorna falso
            sleep(0.100)


class Topo(Thread):

    def __init__(self, s):
        Thread.__init__(self)
        self.striscia = s

    def run(self):
        print("\nFirst run Topo")
        while not self.striscia.muoviTopo():  # chiama la funzione muoviTopo dichiarata sopra fino a quando non ritorna falso
            sleep(0.050)


striscia = Striscia()
jerry = Topo(striscia)
tom = Gatto(striscia)
display = Display(striscia)
print("Created")
display.start()
jerry.start()
tom.start()
print("Started")
sleep(5)
