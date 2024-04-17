from threading import Condition, RLock, Thread
from random import randint
from time import sleep


class BlockingQueue:

    def __init__(self, size):

        # lista che contiene gli elementi inseriti nella coda
        self.elementi = []

        # dimensione massima della coda
        self.size = size

        # RLock che viene utilizzato per disciplinare le invocazioni simultanee ai metodi put e get
        self.lock = RLock()

        # Condizione che viene utilizzata per notificare i thread che attendono che la coda non sia più tutta piena
        self.conditionTuttoPieno = Condition(self.lock)

        # Condizione che viene utilizzata per notificare i thread che attendono che la coda non sia più tutta vuota
        self.conditionTuttoVuoto = Condition(self.lock)

    #
    # Inserisce un elemento nella coda
    # Se la coda è piena, il thread che invoca il metodo put viene bloccato
    # Se la coda non è piena, il thread che invoca il metodo put inserisce l'elemento nella coda e notifica un thread
    # che attende che la coda non sia più tutta vuota
    #
    def put(self, t):
        with self.lock:
            #
            # Se non ci sono slot liberi, il thread che invoca il metodo put viene bloccato
            #
            while len(self.elementi) == self.size:
                self.conditionTuttoPieno.wait()
            #
            # Questo if serve per evitare notify ridondanti
            # Non ci possono essere consumatori in attesa a meno che, un attimo prima della append(t) la coda non fosse
            # totalmente vuota
            # Se non ci sono consumatori in attesa, non c'è bisogno di notificare nessuno
            # Il codice è corretto anche senza questo if, ma ci saranno notify anche quando non necessari
            #
            if len(self.elementi) == 0:
                self.conditionTuttoVuoto.notify()
            self.elementi.append(t)

    #
    # Estrae un elemento dalla coda
    # Se la coda è vuota, il thread che invoca il metodo get viene bloccato
    # Se la coda contiene almeno un elemento, il thread che invoca il metodo get estrae l'elemento dalla coda e notifica
    # un thread che attende che la coda non sia più tutta piena
    #
    def get(self, index):
        with self.lock:
            #
            # Se non ci sono elementi da estrarre, il thread che invoca il metodo get viene bloccato
            #
            while len(self.elementi) == 0:
                self.conditionTuttoVuoto.wait()
            #
            # Questo if serve per evitare notify ridondanti
            # Non ci possono essere produttori in attesa a meno che, un attimo prima della pop(zero) la coda non fosse
            # totalmente piena
            # Se non ci sono produttori in attesa, non c'è bisogno di notificare nessuno
            # Il codice è corretto anche senza questo if, ma ci saranno notify anche quando non necessari
            #
            if len(self.elementi) == self.size:
                self.conditionTuttoPieno.notify()
            return self.elementi.pop(index)


class SalaDiAttesa:
    def __init__(self, posti):
        # crea la coda dei pazienti che necessitano di una visita
        self.CodaVisite = BlockingQueue(posti)
        # crea la coda dei pazienti che necessitano solamente di una ricetta medica
        self.CodaRicette = BlockingQueue(posti)
        # crea la coda dei pazienti che necessitano di una ricetta medica dopo aver fatto una visita dal medico
        self.CodaPrioritaria = BlockingQueue(posti)
        self.lock = RLock()
        self.PazienteDimesso = Condition(self.lock)
        self.SalaAttesaVuota = Condition(self.lock)

    def in_sala_attesa(self, paziente):
        """
        match paziente.prestazione:
            case 0:  # il paziente si mette in coda per una visita
                self.CodaVisite.put(paziente)
            case 1:  # il paziente si mette in coda per una ricetta
                self.CodaRicette.put(paziente)
            case 2:  # il paziente si mette in coda per una ricetta dopo una visita
                self.CodaPrioritaria.put(paziente)
        """
        self.CodaVisite.put(paziente)

    def visita_paziente(self, nome):
        """
        return self.CodaVisite.get(0)  # viene restituito il primo paziente nella coda della visita
        """
        with self.lock:
            if not self.CodaVisite.elementi:
                self.SalaAttesaVuota.wait()

            paziente = self.CodaVisite.get(0)

            match paziente.prestazione:
                case 0:
                    print(f"Il Dr. {nome}: STA VISITANDO il paziente {paziente.nome}")
                    #  sleep(5)
                    if randint(0, 1):
                        print(f"Il Dr. {nome}: HA DIMESSO il paziente {paziente.nome}")
                        paziente.set_prestazione(-1)
                    else:
                        print(f"Il Dr. {nome}: HA PRESCRITTO LA RICETTA al paziente {paziente.nome}")
                        self.CodaPrioritaria.put(paziente)
                case 1:
                    self.CodaRicette.put(paziente)

    def rilascia_ricetta(self):
        if self.CodaPrioritaria.elementi:  # se ci sono pazienti nella coda prioritaria
            return self.CodaPrioritaria.get(0)  # viene restituito il primo paziente nella coda prioritaria
        elif self.CodaRicette:  # se ci sono pazienti nella coda delle ricette
            return self.CodaRicette.get(0)  # viene restituito il primo paziente nella coda delle ricette


prestazioni = ("una VISITA", "una RICETTA", "una RICETTA")


class Paziente(Thread):

    def __init__(self, a, nome):
        super().__init__()
        self.nome = nome
        self.sala_attesa = a
        self.prestazione = randint(0, 1)  # sceglie casualmente "una VISITA" o "una RICETTA"

    def set_prestazione(self, prestazione):  # consente di modificare la variabile prestazione
        with self.sala_attesa.lock:
            # notifica al paziente in attesa se deve rimettersi in coda o è stato dimesso
            self.sala_attesa.PazienteDimesso.notify()
            # prestazione = -1 paziente pronto per essere dimesso
            # prestazione = 2 paziente pronto per entrare nella coda prioritaria
            self.prestazione = prestazione

    def run(self):
        with self.sala_attesa.lock:
            print(f"{self.nome}: è in sala d'attesa per {prestazioni[self.prestazione]}")
            while self.prestazione != -1:
                self.sala_attesa.in_sala_attesa(self)  # il paziente si aggiunge a una coda (ricetta o visita)
                # rimane in stato di wait din quando non viene modificata la variabile prestazione
                self.sala_attesa.SalaAttesaVuota.notify()
                self.sala_attesa.PazienteDimesso.wait()
            print(f"{self.nome}: DIMESSO")


class Medico(Thread):

    def __init__(self, a, nome):
        super().__init__()
        self.nome = nome
        self.sala_attesa = a

    def run(self):
        # fin quando ci sono pazienti nella coda delle visite il Thread rimane attivo dopo termina
        while True:
            self.sala_attesa.visita_paziente(self.nome)
            '''
            paziente = self.sala_attesa.visita_paziente()  # preleva il paziente in posizione 0 dalla coda delle visite
            with self.sala_attesa.lock:
                print(f"Il Dr. {self.nome}: STA VISITANDO il paziente {paziente.nome}")
                if randint(0, 1):  # sceglie casualmente se dimetterlo o metterlo nella coda prioritaria per la ricetta
                    print(f"Il Dr. {self.nome}: HA DIMESSO il paziente {paziente.nome}")
                    paziente.set_prestazione(-1)
                else:
                    print(f"Il Dr. {self.nome}: HA PRESCRITTO LA RICETTA al paziente {paziente.nome}")
                    paziente.set_prestazione(2)
            '''


class Segretaria(Thread):

    def __init__(self, a, nome):
        super().__init__()
        self.nome = nome
        self.sala_attesa = a

    def run(self):
        # fin quando ci sono pazienti in una qualunque delle code il Thread rimane attivo dopo termina
        while True:
            # viene prelevato il primo paziente dalla coda prioritaria fin quando non si svuota
            # se la coda prioritaria è vuota viene prelevato il primo paziente dalla coda delle ricette
            paziente = self.sala_attesa.rilascia_ricetta()
            with self.sala_attesa.lock:
                print(f"La Sig.na. {self.nome}: HA PRESCRITTO LA RICETTA al paziente {paziente.nome}")
            paziente.set_prestazione(-1)  # assegna la paziente la prescrizione -1 che rappresenta le dimissioni


Posti = 20  # posti della sala di attesa

Pediatria = SalaDiAttesa(Posti)

Dr_Miraggio = Medico(Pediatria, "Miraggio")
Dr_Miraggio.start()

Sig_na_bona = Segretaria(Pediatria, "Lucia")
Sig_na_bona.start()
'''
Dr_Delfino = Medico(Pediatria, "Delfino")
Dr_Delfino.start()

Dr_Torrone = Medico(Pediatria, "Torrone")
Dr_Torrone.start()

Sig_na_mala = Segretaria(Pediatria, "Paola")
Sig_na_mala.start()
'''

for i in range(500):  # se vengono creati più Thread paziente rispetto ai posti il programma si blocca (non sempre)
    i += 1
    newPaziente = Paziente(Pediatria, f"Paziente {i}")
    newPaziente.start()
    sleep(0.05)
