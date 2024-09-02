from threading import Thread,RLock
from time import sleep

'''
    Classe Astratta Stampa. StampaNonsafe e Stampadisciplinata ne sono rispettivamente figlia e nipote
'''
class Stampa:
    def __init__(self):
        pass
    def stampa(self,c,l):
        pass
    def stampaStriscia(self,c):
        pass
 
#
# Esempio di uso non sincronizzato delle funzioni di stampa
#  
class StampaNonsafe(Stampa):
    def __init__(self):
        super().__init__()

    def stampa(self, c, l):
        for i in range(0,l+1):
            print(c, end='', flush=True)
            #sleep(0.01)
        print('')
    
    def stampaRighe(self,c,l,r):
        for i in range(r):
            self.stampa(c,l)

    def stampaStriscia(self,c,r=1):
        self.stampaRighe(c,50,r)

 
class StampaDisciplinata(StampaNonsafe):

    def __init__(self):
        super().__init__()
        self.lock = RLock()

    def stampa(self, c, l):
        with self.lock:
            super().stampa(c,l)

    def stampaRighe(self,c,l,r):
        with self.lock:
            super().stampaRighe(c,l,r)


MAXITER = 100
class StampatoreDiAsterischi(Thread):

    def __init__(self,s):
        super().__init__()
        self.st = s
    
    def run(self):
        conta = MAXITER
        while conta > 0 :
            st.stampaStriscia('*')
            conta -= 1

class StampatoreDiTrattini(Thread):

    def __init__(self,s):
        super().__init__()
        self.st = s
     
    def run(self):
        conta = MAXITER
        while conta > 0 :
            st.stampaStriscia('-')
            conta -= 1

class StampatoreDiRighe(Thread):

    def __init__(self,s):
        super().__init__()
        self.st = s
     
    def run(self):
        conta = MAXITER
        while conta > 0:
            st.stampaRighe('@',50,5)
            conta -= 1


#
# Si puÃ² costruire st come StampaNonsafe o come StampaDisciplinata e verificare la differenza
#
#st = StampaNonsafe()
st = StampaDisciplinata()

john = StampatoreDiAsterischi(st)
al   = StampatoreDiTrattini(st)
jack = StampatoreDiRighe(st)

john.start()
al.start()
jack.start()

print("Main Terminato")
 