from threading import RLock, Thread
from random import randint
from time import sleep

GREEN = 0
RED = 1
NUMPLAYERS = 457

class PlayerData:
    def __init__(self, p, n: str):
        self.player = p
        self.num = n
        self.position = 0

class UnDueTreStella:
    def __init__(self):
        self.winningLine = 120
        self.gameDuration = 20
        self.playerData = {}
        self.currentMode = GREEN
        self.running = True
        self.lock = RLock()
        
        for i in range(1, NUMPLAYERS + 1):
            num = "%03d" % i
            pd = PlayerData(Player(self, num), num)
            self.playerData[num] = pd
            pd.player.start()
        
        Timer(self).start()
        
        self.stellaMaster = StellaMaster(self)
        self.stellaMaster.start()
        
        Display(self).start()

    def shout(self, text: str):
        print(text.upper() + "!!!!")

    def step(self, num: str) -> int:
        sleep(randint(0, 5) / 10)
        with self.lock:
            if self.currentMode == GREEN:
                self.playerData[num].position += 1
                if self.playerData[num].position > self.winningLine:
                    self.shout("I'm aliveeeeeeeee. [Player %s survives beyond the line]" % num)
                    return 0
                else:
                    return 1
            else:
                self.shout("Please please no no no no don't kill meeee aaaaaahhhh. [RIP Player %s]" % num)
                self.kill(num)
                return -1

    def getLight(self) -> bool:
        with self.lock:
            return self.currentMode

    def setLight(self, v: int):
        with self.lock:
            self.currentMode = v
            color = "red" if v == RED else "green"
            self.shout(color + " light")

    def stop(self):
        with self.lock:
            self.running = False

    def gameOver(self) -> bool:
        with self.lock:
            return not self.running or len(self.playerData) == 0

    def kill(self, num):
        with self.lock:
            if num in self.playerData:
                self.shout("killing player %s aahahahahaha" % num)
                del self.playerData[num]

    def killPeople(self):
        with self.lock:
            for num in list(self.playerData.keys()):
                if self.playerData[num].position <= self.winningLine:
                    self.kill(num)
                else:
                    print("Sparing player %s" % num)

    def printPlayers(self):
        with self.lock:
            txt = ""
            for pd in self.playerData.values():
                txt += f"%s:%03d " % (pd.num, pd.position)
            print(txt)

class Timer(Thread):
    def __init__(self, game: UnDueTreStella):
        Thread.__init__(self)
        self.game = game

    def run(self):
        sleep(self.game.gameDuration)
        self.game.stop()
        self.game.shout("TIME IS OVER!")

class Player(Thread):
    def __init__(self, game: UnDueTreStella, numero: str):
        Thread.__init__(self)
        self.game = game
        self.numero = numero

    def run(self):
        aliveAndKicking = 1
        while aliveAndKicking > 0:
            if self.game.getLight() == GREEN:
                sleep(0.010)
                aliveAndKicking = self.game.step(self.numero)
        if aliveAndKicking == -1:
            pass
        else:
            pass

class StellaMaster(Thread):
    def __init__(self, game: UnDueTreStella):
        Thread.__init__(self)
        self.game = game

    def run(self):
        while not self.game.gameOver():
            self.game.setLight(GREEN)
            sleep(randint(1, 10) / 5)
            self.game.setLight(RED)
        viviAlloScadere = len(self.game.playerData)
        print("The timer ended with %d survivors. Proceeding to kill survivors still before the winning line." % viviAlloScadere)
        self.game.killPeople()
        viviAllaFine = len(self.game.playerData)
        print(f"%d players participated. There were %d players alive at the end of the time. Then the game ended with %d survivors. Proceeding to next game." % (NUMPLAYERS,viviAlloScadere,viviAllaFine))


class Killer(Thread):
    def __init__(self, game : UnDueTreStella):
        Thread.__init__(self)
        self.game = game()





class Display(Thread):
    def __init__(self, game: UnDueTreStella):
        Thread.__init__(self)
        self.game = game

    def run(self):
        while not self.game.gameOver():
            sleep(1)
            self.game.printPlayers()

theSquidGame = UnDueTreStella()
print("GAME STARTED. GOOD LUCK")