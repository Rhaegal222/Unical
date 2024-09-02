from threading import RLock, Thread, Condition, Barrier
from random import randint,seed
from time import sleep

'''

Il codice fornito implementa il gioco di “Un, due, tre, Stella!”, nella versione resa famosa dalla serie The Squid Game. 
457 diversi Player devono riuscire a compiere un certo numero di passi N entro lo scadere di un certo tempo limite T (gameDuration nel codice). 
Un semaforo che si alterna a intervalli temporali casuali tra i valori RED e GREEN stabilisce i momenti in cui i Player possono muoversi. 
Se un Player si muove in un momento in cui il  semaforo è RED, il Player in questione viene immediatamente eliminato. 
Un Player può invece compiere liberamente dei passi nei momenti in cui il semaforo è GREEN. 
Quando un Player compie più degli N (winningLine nel codice) passi richiesti esso si può considerare salvo. 
Allo scadere del tempo T, tutti i Player che non hanno ancora compiuto i passi richiesti per salvarsi vengono eliminati e infine il gioco termina definitivamente.

'''


GREEN = 0
RED = 1
NUMPLAYERS = 457

#
# Suggerimento per le prove a casa: ridurre il numero di giocatori e variare la durata del gioco e la winningLine.
#


#
# Funzione di stampa di debug
#
debugOn = True
def debug(text : str):
    if debugOn:
        print(text)

#
# Scheda di ciascun giocatore
#
class PlayerData:

    def __init__(self,p, n : str):
        self.player = p
        self.num = n
        self.position = 0
#
# Classe che tiene traccia dello stato del gioco
#
class UnDueTreStella:

    def __init__(self, specialMode = False):

        #
        # Numero di passi che un giocatore deve compiere in tempo per poter salvarsi
        #         
        self.winningLine = 300
        #
        # Tempo a disposizione per poter salvarsi (in secondi)
        #
        self.gameDuration = 20
        #
        # Dizionario che tiene traccia dello stato di ciascun giocatore
        #
        self.playerData = {}
        #
        # Il semaforo può essere RED o GREEN. Inizialmente è GREEN
        #
        self.currentMode = GREEN
        #
        # Il gioco inizia subito e ne teniamo traccia con la variabile running
        #
        self.running = True
        #
        # Lock per proteggere l'accesso a tutte le variabili condivise che stanno in UnDueTreStella
        #
        self.lock = RLock()
        #
        # PUNTO 3: introduco una condizione per segnalare a tutti i thread, tra cui il Timer, che il gioco è finito per qualche motivo.
        # 
        self.condFineGioco = Condition(self.lock)
        #
        #
        # PUNTO 2: condizione su cui un killer aspetta gli ordini di eliminazione
        #
        self.killerCondition = Condition(self.lock)
        #
        # PUNTO 2: introducendo il Killer, bisogna tenere conto a che quando il gioco finisce 
        # bisognerà poi aspettare che il Killer finisca tutte le uccisioni, prima di stampare le statistiche finali e terminare
        #
        self.killerFinished = False
        self.condFineKilling = Condition(self.lock)
        #
        # AGGIUNTA MIGLIORATIVA OPZIONALE: una Barriera per stampare le scritte finali solo quando StellaMaster, Display, Killer, Timer e tutti i Player hanno correttamente finito le loro attività.
        #
        # La barriera si sblocca quando tutti i PLAYERS (NUMPLAYERS) + 1 Killer + 1 Timer + 1 StellaMaster + 1 Display hanno invocato wait.
        #
        self.barrieraFinale = Barrier(NUMPLAYERS+4)
        #
        # Avvio il Thread timer, il quale fermerà il gioco dopo self.gameDuration secondi
        #
        #
        # Punto 3: il Thread Timer viene avviato solo se richiesto
        #
        self.specialMode = specialMode
        if not specialMode:
            Timer(self).start()
        #
        # Punto 2: avvio il thread Killer
        #
        Killer(self).start()
        #
        # Punto 2: introduco una lista di player destinati a essere uccisi
        #
        self.playersToKill = []
        #
        # Punto 3: aggiungo variabile per conteggiare quanti salvi
        #
        self.playerSalvi = 0
        #
        # Creo NUMPLAYERS giocatori, e tengo traccia del loro stato nel dizionario playerData; creo tanti Thread Player corrispondenti e li avvio
        #
        for i in range(1,NUMPLAYERS+1):
            num = "%03d" % i   # num = f"{i:03}"
            pd = PlayerData(Player(self,num),num)
            self.playerData[num] = pd
            pd.player.start()
        #
        # stellaMaster è il Thread che cicla a intervalli casuali il valore del semaforo tra RED e GREEN. Lo creo e lo avvio
        # 
        self.stellaMaster = StellaMaster(self)
        self.stellaMaster.start()
        #
        # Avvio un thread display, il quale mostrerà lo stato del gioco periodicamente.
        #   
        Display(self).start()

    #
    # Metodo per stampare urla concitate
    #    
    def shout(self,text : str):
        print(text.upper()+"!!!!")

    #
    # Ogni Thread Player prova periodicamente a eseguire l'operazione di STEP. Se però l'operazione viene fatta quando il semaforo è RED, si MUORE
    #
    def step(self, num : str) -> int:
        with self.lock:
            #
            # PUNTO 3: cambio le condizioni secondo cui posso fare uno step
            #
            if self.currentMode == GREEN and not (self.specialMode and self.playerSalvi >= 50):
                self.playerData[num].position += 1
                #debug(f"Player {num} stepping to {self.playerData[num].position}")
                if self.playerData[num].position > self.winningLine:
                    #
                    # SAFE! Sono salvo e oltre la linea finale
                    #
                    # PUNTO 3: conteggio i salvi ed eventualmente avvio il Timer. Inoltre blocco il Timer se il gioco finisce perchè ci sono 50 salvi.
                    #
                    self.playerSalvi += 1
                    if self.specialMode and self.playerSalvi == 1:
                        Timer(self).start()
                    if self.specialMode and self.playerSalvi == 50:
                        debug("Notify Fine Gioco 50 Salvi")
                        self.condFineGioco.notifyAll()                   
                    return 0 
                else:
                    #
                    # Sono riuscito a fare un passo in più
                    #
                    return 1
            else: 
                # se si arriva in questo ramo, il semaforo è RED. il Player viene UCCISO
                #
                # Punto 2: la kill non va più fatta direttamente
                #
                # self.kill(num)
                self.ordinaEliminazione(num)
                return -1

    #
    # Metodo per testare il colore attuale del semaforo. Usato dai Player
    #
    def getLight(self) -> int:
        with self.lock:
            return self.currentMode

    #
    #  Metodo per cambiare il colore del semaforo. Usato da StellaMaster
    #
    def setLight(self, v : int):
        with self.lock:
            self.currentMode = v
    #
    # Metodo per interrompere il gioco. Invocato da Timer
    #
    def stop(self):
        with self.lock:
            self.running = False

    #
    # Metodo per verificare se il gioco è finito.
    # Un gioco si considera terminato se sono morti tutti i giocatori, oppure il Timer ha impostato self.running = False
    # Invocato da StellaMaster.
    #
    # Punto 3:
    #
    # se siamo in specialMode, il gioco può terminare per un terzo motivo, e cioè i giocatori salvi sono esattamente 50.
    #
    def gameOver(self) -> bool:
        with self.lock:
            fine = not self.running or len(self.playerData) == 0 or (self.specialMode and self.playerSalvi == 50)
            if fine:
                self.condFineGioco.notifyAll()
            return fine

    #
    # Metodo che uccide un player ed elimina i suoi dati da playerData. Invocato in due casi:
    #    -dall'interno di step() quando si fa un passo falso con luce RED
    #    -a tempo scaduto quando il player è rimasto dietro la linea di salvezza
    #
    def kill(self,num):
        with self.lock:
            debug(f"Trying to kill {num}")
            if num in self.playerData:
                self.shout("killing player %s aahahahahaha" % num)   # self.shout(f"killing player {num} aahahahahaha")
                del self.playerData[num]
            #else: 
            #    print(f"Player {num} is dead already")
    #
    # Uccide tutti i player che a tempo scaduto si trovano ancora dietro la linea di salvezza. Invocato da stellaMaster
    #
    def killPeople(self):
        with self.lock:
            debug("Start ordina ultime uccisioni")
            #
            # Non si possono cancellare elementi da un dizionario mentre vi si sta iterando sopra. 
            # dunque è necessario prima ricopiare tutte le chiavi in una nuova lista separata.
            #
            for num in list(self.playerData.keys()):
                #
                #  Giocatore che non si è salvato. Lo eliminiamo
                #
                if self.playerData[num].position <= self.winningLine:
                    #
                    # Punto 2:
                    #
                    #self.kill(num)
                    debug(f"Ordina uccisione {num}")
                    self.ordinaEliminazione(num)
                #
                #  Giocatore che si è salvato.
                #
                else:
                    print("Sparing player %s" % num)     # print(f"Sparing player {num}")
            #
            # Punto 2: aggiunge il valore "000" che indica fine lista dei player da uccidere attende che il Killer abbia concluso tutte le ammazzatine commissionate.
            #
            debug("Ordina uccisione 000")
            self.ordinaEliminazione("000")
            while not self.killerFinished:
                self.condFineKilling.wait()
            debug("Fine kill residui")
    
    #
    # Punto 2: funzione per ordinare l'eliminazione. Si noti che per scelta, non si mette limite al numero di player che possono stare in coda in attesa di uccisione
    # 
    def ordinaEliminazione(self,num : str):
        with self.lock:
            debug(f"Ordino eliminazione {num}")
            self.playersToKill.append(num)
            self.killerCondition.notifyAll()

    #
    # Punto 2: il killer usa questa funzione per attendere gli ordini di eliminazione ed eseguirli. 
    # La funzione ritorna False quando sono finiti anche tutti i Player da eliminare. Viene usato il valore -1 per mettere in coda il segnale di "ultimo player".
    # 
    def waitAndKill(self):
        with self.lock:
            debug(f"Entro in wait and kill")
            while len(self.playersToKill) == 0:
                self.killerCondition.wait()
                debug(f"Notify ordine")

            debug(f"Eseguo ordine di uccisione {self.playersToKill[0]}")
            if self.playersToKill[0] == "000":
                debug("FINE KILLER")
                self.killerFinished = True
                self.condFineKilling.notifyAll()
                return False
            if len(self.playersToKill) > 0:
                self.kill(self.playersToKill.pop(0))
                return True
            
    #
    # PUNTO 3: aggiunta di una sleep modificata che termina in due casi: 1. passa il tempo prescritto, oppure 2. il gioco termina per qualche motivo
    #
    def sleepTimer(self):
        with self.lock:
            self.condFineGioco.wait(self.gameDuration)
    #
    # Stampa la situazione di gioco attuale. Per ogni giocatore viene stampato il numero corrispondente e il numero di passi fatti
    # Esempio: 045:013 => Il giocatore 045 ha compiuto 13 passi finora.
    # Invocato da Display
    #
    def printPlayers(self):
        with self.lock:
            txt = ""
            for pd in self.playerData.values():
                txt += f"%s:%03d " % (pd.num,pd.position)   #  txt += f"{pd.num}:{pd.position:03} "
            print(txt)    

    def barrierWait(self):
        self.barrieraFinale.wait()

#
# Thread il cui unico scopo è arrestare il gioco al termine di un periodo di durata scelta
#
class Timer(Thread):

    def __init__(self,game : UnDueTreStella):
        Thread.__init__(self)
        self.game = game

    def run(self):
        debug("Timer started")
        self.game.sleepTimer()
        self.game.stop()
        self.game.shout("TIME IS OVER!")
        self.game.barrierWait()


class Killer(Thread):

    def __init__(self,game : UnDueTreStella):
        Thread.__init__(self)
        self.game = game

    def run(self):

        while self.game.waitAndKill():
            pass
        debug("Killer FINISHED")
        self.game.barrierWait()




#
# Thread giocatore
#
class Player(Thread):

    def __init__(self,game : UnDueTreStella, numero : str):
        Thread.__init__(self)
        self.game = game
        self.numero = numero

    #
    #  Il ciclo di vita di un giocatore è il seguente:
    #       -verifico che la luce sia verde
    #       -se sì, provo a fare uno step
    #
    #  step può restituire tre valori diversi che finiscono nella variabile aliveAndKicking, in dipendenza dei quali il Player si regola di conseguenza:
    #   
    #   aliveAndKicking = 1. Tutto OK per ora, continua a fare step
    #   aliveAndKicking = -1. L'ultimo step è fallito, sono MORTO, dunque il thread termina
    #   aliveAndKicking = 0. Il Player ha superato la linea. E' salvo e il thread può terminare
    #
    def run(self):
        debug("Player %s started" % self.numero)  #  debug(f"Player {self.numero} started")
        aliveAndKicking = 1
        while aliveAndKicking > 0:
            if self.game.getLight() == GREEN:
                #
                # Questa sleep riduce la prontezza di riflessi di un Player, aumentando la probabilità di trovare la luce RED quando viene effettuato uno step
                #
                sleep(randint(0,5)/10)
                aliveAndKicking = self.game.step(self.numero)
        if aliveAndKicking == -1:
            self.game.shout("Please please no no no no don't kill meeee aaaaaahhhh. [RIP Player %s]" % self.numero)  #self.game.shout(f"Please please no no no no don't kill meeee aaaaaahhhh. [RIP Player {self.numero}]")
        else:
            self.game.shout("I'm aliveeeeeeeee. [Player %s survives beyond the line]" % self.numero)     #self.game.shout(f"I'm aliveeeeeeeee. [Player {self.numero} survives beyond the line]")
        self.game.barrierWait()


class StellaMaster(Thread):

    def __init__(self,game : UnDueTreStella):
        Thread.__init__(self)
        self.game = game
    #
    # Lo StellaMaster è il thread che gestisce il semaforo. 
    # Fintantochè il gioco non è gameOver() lo StellaMaster alterna tra RED e GREEN LIGHT a intervalli di tempo casuali
    # Quando il gioco finisce (il timer scade, oppure sono morti tutti)
    # lo StellaMaster invoca killPeople() e uccide tutti i Player che sono rimasti dietro la linea allo scadere del tempo
    #
    def run(self):
        debug("StellaMaster Started")
        while not self.game.gameOver():
            self.game.shout("green light")
            self.game.setLight(GREEN)
            sleep(randint(1,10)/5)
            self.game.shout("red light")
            self.game.setLight(RED)
        viviAlloScadere = len(self.game.playerData)
        print("The timer ended with %d survivors. Proceeding to kill survivors still before the winning line." % viviAlloScadere)
        self.game.killPeople()
        #
        # Punto 2: si noti che killPeople termina solo quando il Killer ha effettuato tutte le uccisioni rimaste
        #
        #print(f"The game ended with {len(self.game.playerData)} survivors. Proceeding to next game.")
        viviAllaFine = len(self.game.playerData)
        self.game.barrierWait()
        print(f"%d players participated. There were %d players alive at the end of the time. Then the game ended with %d survivors. Proceeding to next game." % (NUMPLAYERS,viviAlloScadere,viviAllaFine))

#
# Il Thread Display visualizza lo stato del gioco a intervalli di un secondo.
#
class Display(Thread):

    def __init__(self,game : UnDueTreStella):
        Thread.__init__(self)
        self.game = game

    def run(self):
        while(not self.game.gameOver()):
            sleep(1)
            self.game.printPlayers()
        self.game.barrierWait()


seed()
theSquidGame = UnDueTreStella(True)
print ("GAME STARTED. GOOD LUCK")