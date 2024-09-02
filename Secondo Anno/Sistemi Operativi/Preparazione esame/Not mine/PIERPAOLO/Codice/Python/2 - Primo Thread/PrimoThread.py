from threading import Thread
from threading import Lock

class Stampa:
    def __init__(self): 
        self.lock=Lock()    # "la porta del bagno"

    def stampa(self,c,l):  
        self.lock.acquire()
        for i in range(0,l+1):
            print( c, end='')
        print('')
        self.lock.release()
    def stampaStriscia(self,c):
        self.stampa(c,50)


class Stampatore(Thread):

    def __init__(self,s : Stampa, c):
        super().__init__()
        self.st = s
        self.count = 0
        self.c=c

    def run(self):
        while True:
            self.st.stampaStriscia(self.c)


st = Stampa()

john = Stampatore(st,"*")
al = Stampatore(st,"-")
john.start()
al.start()

print("Main terminato")