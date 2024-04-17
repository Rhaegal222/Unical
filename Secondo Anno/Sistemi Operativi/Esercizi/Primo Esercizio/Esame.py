class Esame:
    def __init__(self, nome, cfu, voto=0):
        self.nome=nome
        self.cfu=cfu
        self.voto=voto

    def print(self):
        print("Esame:\t\t %s \t Voto: %d \t CFU: %d" % (self.nome, self.voto, self.cfu))

    def __eq__(self, other):
        return (self.nome==other.nome) and (self.cfu==other.cfu)

    def __ne__(self, other):
        return not (self == other)