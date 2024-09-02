from threading import Thread,Lock
from time import sleep
from random import random,randrange

'''
    Soluzione commentata esercizio sul gioco delle sedie. 
    In questo sorgente potete sperimentare con tre possibili soluzioni: soluzione A senza lock (sbagliata), soluzione B con i lock ma usati male (sbagliata), soluzione C con i lock usati bene (corretta)

    Soluzione A:
        - Fatta creando un array di PostoUnsafe e usando come thread PartecipanteUnsafe

        In questa soluzione non viene usata alcuna forma di locking. Facendo girare il gioco piÃ¹ volte, riscontrerete che a volte tutti i Partecipanti riescono a sedersi, 
        poichÃ¨ qualcuno si siede sulla stessa sedia

    Soluzione B:
        - Fatta creando un array di PostoQuasiSafe e usando come thread PartecipanteUnSafe

        Questa soluzione ha lo stesso problema della soluzione A. 
        Anche se libero() e set() sono, prese singolarmente, thread-safe, queste vengono chiamate in due tempi distinti (PRIMO TEMPO: chiamata a libero; SECONDO TEMPO: chiamata a set() ), acquisendo e rilasciando il lock entrambe le volte. 
        In mezzo ai due tempi, eventuali altri partecipanti avranno la possibilitÃ  di acquisire il lock su self.posti[i] e modificarne lo stato. Noi non vogliamo questo. E' una race condition.


    Soluzione C:
        - Fatta usando un array di PostoSafe e usando come thread PartecipanteSafe

'''

class PostoUnsafe:

    def __init__(self):
        self.occupato = False

    def libero(self):
        return not self.occupato
           
    def set(self,v):
        self.occupato = v
        

class PostoQuasiSafe(PostoUnsafe):

    def __init__(self):
        super().__init__()
        self.lock = Lock()

    def libero(self):
        '''
        Il blocco "with self.lock" Ã¨ equivalente a circondare tutte le istruzioni in esso contenute con self.lock.acquire() e self.lock.release()
        Notate che questo costrutto Ã¨ molto comodo in presenza di return, poichÃ¨ self.lock.release() verrÃ  eseguita DOPO la return, cosa che normalmente
        non sarebbe possibile (return normalmente Ã¨ l'ultima istruzione di una funzione)
        '''
        with self.lock:
            return super().libero()
           
    def set(self,v):
        self.lock.acquire()
        super().set(v)
        self.lock.release()

class PostoSafe(PostoQuasiSafe):

    def __init__(self):
        super().__init__()

    def testaEoccupa(self):
        with self.lock:
            if (self.occupato):
                return False
            else:
                self.occupato = True
                return True


class Display(Thread):

    def __init__(self,posti):
        super().__init__()
        self.posti = posti

    def run(self):
        while(True):
            sleep(1)
            for i in range(0,len(self.posti)):
                if self.posti[i].libero():
                    print("-", end='', flush=True)
                else:
                    print("o", end='', flush=True)
            print('')


class PartecipanteUnsafe(Thread):

    def __init__(self,posti):
        super().__init__()
        self.posti = posti

    def run(self):
        sleep(randrange(5))
        for i in range(0,len(self.posti)):
            #
            # Errore. Anche se libero() e set() sono, prese singolarmente, thread-safe, queste vengono chiamate in due tempi distinti (PRIMO TEMPO: chiamata a libero; SECONDO TEMPO: chiamata a set() ), acquisendo e rilasciando il lock entrambe le volte. 
            # In mezzo ai due tempi, eventuali altri partecipanti avranno la possibilitÃ  di acquisire il lock di self.posti[i] e modificarne lo stato. Noi non vogliamo questo. E' una race condition.
            #
            if self.posti[i].libero():
                self.posti[i].set(True)
                print( "Sono il Thread %s. Occupo il posto %d" % ( self.name, i ) )
                return                
        
        print( "Sono il Thread %s. HO PERSO" % self.name)


class PartecipanteSafe(Thread):

    def __init__(self,posti):
        super().__init__()
        self.posti = posti

    def run(self):
        sleep(randrange(5))
        for i in range(0,len(self.posti)):
            if self.posti[i].testaEoccupa():
                print( "Sono il Thread %s. Occupo il posto %d" % ( self.name, i ) )
                return                
        
        print( "Sono il Thread %s. HO PERSO" % self.name )
        print( "Sono il Thread %s. HO PERSO" % self.name )

NSEDIE = 10

#
# Qui si puÃ² sperimentare con i vari tipi di posti e verificare se si verificano delle race condition
#
#
# Soluzione A
#posti = [PostoUnsafe()    for i in range(0,NSEDIE)]
# Soluzione B
#posti = [PostoQuasiSafe() for i in range(0,NSEDIE)]
# Soluzione C
posti = [PostoSafe()      for i in range(0,NSEDIE)]

lg = Display(posti)
lg.start()

#
# I partecipantiSafe accedono ai posti senza race condition. I PartecipantiUnsafe NO.
#
# Per le soluzioni A e B usare PartecipanteUnsafe
# Per la soluzione C usare PartecipanteSafe
#
#
for t in range(0,NSEDIE+1):
    #t = PartecipanteUnsafe(posti)
    t = PartecipanteSafe(posti)
    t.start()

