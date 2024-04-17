from threading import Thread, RLock
from time import sleep
'''
    Classe Astratta Stampa. StampaNonsafe e Stampadisciplinata ne sono rispettivamente figlia e nipote
'''


class Stampa:
    def __init__(self):
        pass

    def stampa(self):
        pass

    def stampaStriscia(self):
        pass


#
# Esempio di uso non sincronizzato delle funzioni di stampa
#  

class StampaNonsafe(Stampa):
    def __init__(self):
        super().__init__()

    def stampa(self, c, l):
        for i in range(0, l + 1):
            print(c, end='', flush=True)
            # sleep(0.01)
        print('')

    def stampaStriscia(self, c):
        self.stampa(c, 50)


class StampaDisciplinata(StampaNonsafe):

    def __init__(self):
        super().__init__()
        #
        # RLock è simile a Lock ma RIENTRANTE: può essere acquisito più volte consecutive dallo stesso thread
        #
        self.lock = RLock()

    def stampa(self, c, l):
        self.lock.acquire()
        super().stampa(c, l)
        self.lock.release()


class StampatoreDiAsterischi(Thread):

    def __init__(self, s: Stampa):
        super().__init__()
        self.st = s
        self.count = 0

    def run(self):
        while True:
            self.st.stampaStriscia('*')


class StampatoreDiTrattini(Thread):

    def __init__(self, s: Stampa):
        super().__init__()
        self.st = s
        self.count = 0

    def run(self):
        while True:
            self.st.stampaStriscia('-')


#
# Si può costruire st come StampaNonsafe o come StampaDisciplinata e verificare la differenza
#
#st = StampaNonsafe()
st = StampaDisciplinata()

john = StampatoreDiAsterischi(st)
al = StampatoreDiTrattini(st)

john.start()  # start serve per schedulare il thread e passa all'istuzione successiva
al.start()

print("Main Terminato")
