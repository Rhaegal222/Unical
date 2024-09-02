from threading import Thread,RLock, Condition, get_ident
from random import randint

"""
#
# Questo è il codice del Thread Stampatore. E' previsto una unica istanza che effettua le stampe
#
"""
class Stampatore(Thread):

    def __init__(self,SP):
        super().__init__()
        self.SP = SP

    #
    # Modificato per risolvere la domanda 1
    #
    def run(self):
        ancora = True
        while(ancora):
            (ancora,s) = self.SP.prelevaStampa()
            if ancora:
                print(s)


"""
#   Ci sono in tutto tre code di attesa per le stampe: 0 = alta pr., 1 = media pr., 2 = bassa pr.
#    NUMERO BASSO = MAGGIORE PRIORITA
#
"""
class StampaPrioritaria:

    
    NCODE = 3
    """
       La traccia prescrive che per le stampe a media priorità, sia possibile effettuare comunque una stampa ogni 5 a priorità più alta, 
       Mentre per le stampe a bassa priorità, questa analoga soglia è 10.
       Queste soglie sono codificate nell'array SOGLIE   
    """
    SOGLIE = [0,5,10]

    def __init__(self,n):
        
        """
            Parte aggiunta per implementare stop()
        """
        self.statoDiArresto = False
    
        """
            Dimensione massima di ogni coda 
        """
        self.size = n
        """
            Le tre code saranno rispettivamente C[0], C[1] e C[2].
        """
        self.C = []
        """
            Le attese ci dicono quante stampe sono state effettuate consecutivamente 
            a priorita minore di i senza che una stampa a priorità i sia stata fatta.
            Esempio: attese[2] = 12 indica che sono state fatte 12 stampe consecutive 
            a priorità 0 e 1 senza che sia stata mai fatta una stampa a priorità 2  
        """
        self.attese = []
        """
            Useremo L come unico lock per garantire la thread safety
        """
        self.L = RLock()
        """
            Se non ci sono stampe da fare, il thread Stampatore aspetterà su questa condition
        """
        self.condEmpty = Condition(self.L)
        """
            Ci sarà invece una condizione di attesa per ciascuna coda nel caso in cui questa sia piena. 
            Esempio, se C[1] è piena, aspetto su condFull[1].
        """
        self.condFull = []
        #
        # Aggiunte per implementare waitForPrint()
        #
        self.aspettoStampa = []
        self.condAttendiStampa = []
        """
            Qui riempio opportunamente C, condFull e attese
        """
        for i in range(0,self.NCODE):
            self.C.append([])
            self.condFull.append(Condition(self.L))
            self.condAttendiStampa.append(Condition(self.L))
            self.attese.append(0)
            self.aspettoStampa.append(False)
        """
            Creo e avvio l'unico thread stampatore
        """
        self.printer = Stampatore(self)
        self.printer.start()
        
    """
        Metodo privato che mi restituisce len(C[0]) + len(C[1]) + len(C[2]) 
    """
    def __totLen(self) -> int:
        retVal = 0
        for i in range(0,self.NCODE):
            retVal += len(self.C[i])
        return retVal

    """
        Metodo privato che mi dice se NON ci sono stampe a priorità più bassa di una certa priorità p che sono in attesa da troppo tempo
        Esempio, supponiamo che p = 0, len(C[1]) = 1, len(C[2]) = 0, attese [0,6,0]
        siccome c'è una stampa a priorità 1 che aspetta da 6 "giri", allora restituisco False, e cioè non posso eseguire una stampa a livello p=0
        poichè ci sono stampe a priorità più bassa, ma che aspettano da troppo tempo.
    """
    def __noAltreSoglieSuperate(self,p : int) -> bool:
        for q in range(p+1,self.NCODE):
            if len(self.C[q]) > 0 and self.attese[q] >= self.SOGLIE[q]:
                return False
        return True 
        
    """
        Questo metodo pone la stringa s a priorità prio nel buffer C[prio]. 
        Si mette in attesa bloccante se in C[prio] non c'è posto.
    """
    def stampa(self, s: str, prio: int):
        with self.L:
            if not self.statoDiArresto:
                while len(self.C[prio]) == self.size:
                    self.condFull[prio].wait()
                self.C[prio].append(s)
                #print(f"{self.C[prio]}")
                self.condEmpty.notify()
  
    """
        Il thread stampatore sceglie la prossima stampa da effettuare grazie a questo metodo 
    """
    #
    # Per risolvere la domanda 1, prelevaStampa restituisce una coppia (bool,str). Se bool = False, le stampe sono finite
    #
    def prelevaStampa(self):
        with self.L:
            """
                Attendo se non ci sono stampe in nessuna coda
            """
            #
            # Se le stampe sono finite ed è stato chiamato stop()
            #
            if self.statoDiArresto and self.__totLen() == 0:
                return (False,"")
            else:
                while self.__totLen() == 0:
                    self.condEmpty.wait() 

            """
                Ciclo sulle tre code partendo da quella a priorità più alta.
            """
            for p in range(0,self.NCODE):
                """
                    Posso stampare a priorità p ?
                    Per poter stampare a priorità p: 
                        -devo avere qualche stampa in attesa su questa priorità (len(C[p]) > 0) e inoltre:
                        -NON ci devono essere in attesa da troppo tempo delle stampe a livello p+1 a salire
                    
                """
                if len(self.C[p]) > 0 and self.__noAltreSoglieSuperate(p):
                    """
                        OK, se sono qui, posso stampare a priorità p. Procedo ad aggiornare le attese sulle priorità da p+1 a salire
                    """
                    for q in range(p+1,self.NCODE):
                        if len(self.C[q]) > 0:
                            self.attese[q] += 1
                    """
                        Finalmente ho stampato a livello p, quindi azzero attese[p]
                    """
                    self.attese[p] = 0
                    """
                        Se in questo momento C[p] è piena, vuol dire che sto per fare un pop() che potrebbe
                        sbloccare un thread in attesa di trovare posto su C[p]. Quindi faccio notify()
                    """
                    if len(self.C[p]) == self.size:
                        self.condFull[p].notify()
                    """
                        Infine, estraggo un elemento da C[p] e lo restituisco
                    """
                    #
                    # Parte aggiunta per realizzare waitForPrint()
                    #
                    self.aspettoStampa[p] = False
                    self.condAttendiStampa[p].notifyAll()
                    #
                    #
                    return (True,self.C[p].pop(0))
    
    """
        Soluzione alla domanda 1
    """
    def stop(self):
        with self.L:
            self.statoDiArresto = True
    
    """
        Soluzione alla domanda 2
    """
    def boost(self,p : int):
        with self.L:
            if p > 0:
                e = self.C[p].pop(0)
                self.stampa(e,p-1)

    """
        Soluzione alla domanda 3
    """
    def waitForPrint(self, p : int):
        with self.L:
            self.aspettoStampa[p] = True
            while(self.aspettoStampa[p]):
                self.condAttendiStampa[p].wait()

"""
    ClientThread è giusto una tipologia di thread di esempio che sorteggia una priorità casuale e produce stampe a quella priorità
"""
class clientThread(Thread):

    def __init__(self,SP):
        super().__init__()
        self.SP = SP
        self.p = randint(0,StampaPrioritaria.NCODE-1)

    def run(self):
        print(f"Stampa n.1 del Thread {get_ident()} con priorità {self.p}")
        self.SP.stampa(f"Stampa n.1 del Thread {get_ident()} con priorità {self.p}",self.p)
        count = 1
        while(True):
            count += 1
            self.SP.stampa(f"Stampa n.{count} del Thread {get_ident()} con priorità {self.p}", self.p)

"""
    Questo è un main di esempio che crea una istanza di StampaPrioritaria e dei ClientThread che ne fanno uso
"""

if __name__ == '__main__':
    stampa = StampaPrioritaria(10)
    for t in range(0,5):
        clientThread(stampa).start()
            