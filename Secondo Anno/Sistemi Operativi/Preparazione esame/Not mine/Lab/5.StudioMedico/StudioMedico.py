from threading import * 
from time import sleep
from random import randint
class SalaAttesa():
    def __init__(self): #passa il paziente
        self.lock = Lock()      # Il lock bisogna dichiararlo SEMPRE nella risorsa a cui dobbiamo accedere
        self.filaSegretaria= BlockingQueue(20)
        self.filaSegretariaP= BlockingQueue(20)
        self.filaMedico= BlockingQueue(20)
    def putPaziente(self,p):
        if(p.ricetta):
            self.filaSegretaria.put(p)
        else: 
            self.filaMedico.put(p)


class Paziente(Thread):
    def __init__(self,nome,ricetta):
        super.__init__()
        self.nome=nome
        self.ricetta=bool(randint(0,1)) #ricetta= true -> ricetta , ricetta=false -> visita

class Medico(Thread):
    def __init__(self):
        pass

class Segretaria(Thread):
    def __init__(self):
        pass

class BlockingQueue():

    def __init__(self,size):

        # lista che contiene i pazienti nella coda
        self.elementi = []

        # dimensione massima della coda
        self.size = size
        # un thread può acquisire un RLock più volte (prima di finire tutto il blocco di codice), purché lo rilasci un numero uguale di volte
        # RLock che viene utilizzato per disciplinare le invocazioni simultanee ai metodi put e get
        self.lock = RLock()

        # Condizione che viene utilizzata per notificare i thread che attendono che la coda non sia piÃ¹ tutta piena
        self.conditionTuttoPieno = Condition(self.lock)

        # Condizione che viene utilizzata per notificare i thread che attendono che la coda non sia piÃ¹ tutta vuota
        self.conditionTuttoVuoto = Condition(self.lock)
    #
    # Inserisce un elemento nella coda
    # Se la coda Ã¨ piena, il thread che invoca il metodo put viene bloccato
    # Se la coda non Ã¨ piena, il thread che invoca il metodo put inserisce l'elemento nella coda e notifica un thread che attende che la coda non sia piÃ¹ tutta vuota
    #
    def put(self,t):
        with self.lock:
            #
            # Se non ci sono slot liberi, il thread che invoca il metodo put viene bloccato
            #
            while len(self.elementi) == self.size:
                self.conditionTuttoPieno.wait()
            #
            # Questo if serve per evitare notify ridondanti
            # Non ci possono essere consumatori in attesa a meno che, un attimo prima della append(t) la coda non fosse totalmente vuota
            # Se non ci sono consumatori in attesa, non c'Ã¨ bisogno di notificare nessuno
            # Il codice Ã¨ corretto anche senza questo if, ma ci saranno notify anche quando non necessari
            #
            if len(self.elementi) == 0:
                self.conditionTuttoVuoto.notify()
            self.elementi.append(t)

    #
    # Estrae un elemento dalla coda
    # Se la coda Ã¨ vuota, il thread che invoca il metodo get viene bloccato
    # Se la coda contiene almeno un elemento, il thread che invoca il metodo get estrae l'elemento dalla coda e notifica un thread che attende che la coda non sia piÃ¹ tutta piena
    #
    def get(self):
        with self.lock:
            #
            # Se non ci sono elementi da estrarre, il thread che invoca il metodo get viene bloccato
            #
            while len(self.elementi) == 0:
                self.conditionTuttoVuoto.wait()
            #
            # Questo if serve per evitare notify ridondanti
            # Non ci possono essere produttori in attesa a meno che, un attimo prima della pop(0) la coda non fosse totalmente piena
            # Se non ci sono produttori in attesa, non c'Ã¨ bisogno di notificare nessuno
            # Il codice Ã¨ corretto anche senza questo if, ma ci saranno notify anche quando non necessari
            #
            if len(self.elementi) == self.size:
                self.conditionTuttoPieno.notify()
            return self.elementi.pop(0)


salaAttesa= SalaAttesa
for i in range (10):
    p=Paziente
    salaAttesa.putPaziente(p)