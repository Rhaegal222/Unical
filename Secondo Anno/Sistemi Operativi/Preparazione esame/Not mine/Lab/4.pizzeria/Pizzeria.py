from threading import *
from queue import *
class BlockingQueue:
    def __init__(self, O):
        self.lock=Lock()
        self.O=O #size
        self.BO=Queue(maxsize=O)#creo buffer (BO) di max 10 pizze
    def addOrdine(self,nomePizza, quantità):
        ordine = (nomePizza, quantità)#tupla per ogni ordine
        self.BO.put(ordine)#mette l'ordine nel buffer
    def putOrdine(self):
        return




#main