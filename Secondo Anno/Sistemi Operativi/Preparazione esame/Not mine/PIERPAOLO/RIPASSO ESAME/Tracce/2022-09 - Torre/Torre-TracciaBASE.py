from threading import Thread,Condition,RLock
from time import sleep

debug = True
#
# Funzione di stampa sincronizzata di debug
#
plock = RLock()
def prints(s):
    plock.acquire()
    if debug:
        print(s)
    plock.release()


class TorreInCostruzione:
    
    def __init__(self,H : int):
        self.altFinale = H
        self.larghezzaFinale = 3
        self.stratoAttuale = 0
        self.tipiStrato = ['-','*']          # oscilleremo tra 0 e 1
        self.torre = ['']                    # il primo strato sarà self.torre[0], inizialmente impostato a ''
        self.tipoStratoAttualmenteUsato = 0  # modalità iniziale = cemento, poichè self.tipiStrato[0] = '-'
        self.terminato = False               # imposteremo self.terminato = True quando la Torre sarà completa
        self.lock = RLock()
        '''
            Condizione su cui un operaio aspetta quando non tocca a lui, 
            ad esempio quando sei un Cementatore ma attualmente è in corso uno strato di mattoni
        '''
        self.attendiTurno = Condition(self.lock)
        '''
            Condizione su cui ci si mette in attesa quando si vuole esser svegliati solo se la Torre è del tutto completa
        '''
        self.attendiFine = Condition(self.lock)
        

    def printTorre(self):
        prints(self.torre)

    '''
        Metodo utilizzato dal main thread per non restituire la Torre prima che sia completata 
    '''
    def attendiTerminazione(self):
        with self.lock:
            while not self.terminato:
                self.attendiFine.wait()
    '''
        addPezzo consente di aggiungere un pezzo alla torre in costruzione corrente. 
        Quando la torre è completa, addPezzo restituisce False. Il valore restituito da addPezzo è usato dagli 
        Operai per determinare quando è necessario fermarsi poichè la Torre è completa 
    '''
    def addPezzo(self,c) -> bool:
        with self.lock:
            '''
                Se non è il mio turno AND la torre è da finire -> aspetto
                Se è il mio turno OR la torre è finita -> non aspetto
                Dopo avere atteso, controllo se per caso non ci sono pezzetti da aggiungere: in tal caso pongo Terminato = True, esco e restituisco False;
                Altrimenti aggiungo il mio pezzetto e restituisco True 
            '''
            while self.tipiStrato[self.tipoStratoAttualmenteUsato] != c and not self.terminato:
                self.attendiTurno.wait()

            if self.stratoAttuale == self.altFinale - 1 and len(self.torre[self.stratoAttuale]) == self.larghezzaFinale:
                #
                # Se siamo arrivati all'ultimo strato AND è stato aggiunto l'ultimo pezzetto dell'ultimo strato, allora:
                #
                # non c'è più lavoro per me nè per nessuno
                #
                self.terminato = True
                #
                # Devo ricordarmi di svegliare tutti gli operai che aspettano per lavorare, e di svegliare il main Thread.
                #
                self.attendiTurno.notifyAll()
                self.attendiFine.notifyAll()
                return False
            #
            #   Aggiungo il mio pezzetto - nota che se arrivi su questo rigo non può essere che lo stratoAttuale sia completo
            #
            self.torre[self.stratoAttuale] = self.torre[self.stratoAttuale] + c

            #
            #  Se è finito lo strato attuale, ma rimane almeno un altro strato da riempire: aggiorno lo stratoAttuale, e
            #  cambio il tipo di strato da Cemento a Mattoni, o viceversa
            #
            if len(self.torre[self.stratoAttuale]) == self.larghezzaFinale and self.stratoAttuale < self.altFinale - 1:
                self.stratoAttuale += 1
                self.torre.append( '' ) # predispongo il prossimo strato 
                self.tipoStratoAttualmenteUsato = (self.tipoStratoAttualmenteUsato + 1) % 2
                self.attendiTurno.notifyAll()

            self.printTorre()

            return True

class Operaio(Thread):
    

    '''
        Un Operaio è un thread che aggiunge pezzi generici a una torre data.
        t = torre da costruire
        tp = simbolo che aggiunge questo operaio, es. tp= '*', oppure tp = '-', ecc. ecc.        
        d = durata che ci vuole per aggiungere un simbolo. es. d=25ms, oppure d=50ms ecc. ecc. 
    '''  
    def __init__(self,t : TorreInCostruzione, tp : str, d:int):
        super().__init__()
        self.torre = t
        self.tipo = tp
        self.durata = d
    
    def run(self):
        '''
            Ciclo in cui un operaio aggiunge un pezzo per volta
        '''
        while(self.torre.addPezzo(self.tipo)):
            sleep(self.durata/1000)
        prints("Thread di tipo: '%s' finito" % self.tipo) 
           
class Cementatore(Operaio):
    '''
        Un cementatore è un Operaio che usa il simbolo '-' e ha una cadenza di un pezzo ogni 25ms
    '''
    def __init__(self, t: TorreInCostruzione):
        super().__init__(t,'-',25)

class Mattonatore(Operaio):

    '''
        Un Mattonatore è un Operaio che usa il simbolo '*' e ha una cadenza di un pezzo ogni 50ms
    '''
    def __init__(self, t: TorreInCostruzione):
        super().__init__(t,'*',50)


class Torre:
    
    def __init__(self):
        pass
        
        
    def makeTorre(self,H:int, M:int, C:int): 
        t = TorreInCostruzione(H)
        Mattonatori = [Mattonatore(t) for _ in range(M)]
        Cementatori = [Cementatore(t) for _ in range(C)]
        for m in Mattonatori:
            m.start()
        for c in Cementatori:
            c.start()
        t.attendiTerminazione()
        return t.torre
        
if __name__ == '__main__':
    T = Torre()
    print (T.makeTorre(90,4,7)) 
    prints("TORRE FINITA")
    