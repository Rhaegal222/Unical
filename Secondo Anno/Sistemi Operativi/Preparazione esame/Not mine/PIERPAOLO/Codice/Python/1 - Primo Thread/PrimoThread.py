from threading import Thread


class Stampa:
    def __init__(self):
        pass

    def stampa(self,c,l):
        for i in range(0,l+1):
            print( c, end='', flush=True)
        print('')

    def stampaStriscia(self,c):
        self.stampa(c,50)


class StampatoreDiAsterischi(Thread):

    def __init__(self,s : Stampa):
        super().__init__()
        self.st = s
        self.count = 0

    def run(self):
        while True:
            self.st.stampaStriscia('*')

class StampatoreDiTrattini(Thread):

    def __init__(self, s : Stampa):
        super().__init__()
        self.st = s
        self.count = 0

    def run(self):
        while True:
            self.st.stampaStriscia('-')



st = Stampa()

john = StampatoreDiAsterischi(st)
al = StampatoreDiTrattini(st)

john.start()
al.start()

print("Main terminato")


    