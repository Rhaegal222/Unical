class Persona:
    numero=0

    def __init__(self, cf, nome, cognome, eta):
        self._cf=cf
        self.__nome=nome
        self.cognome=cognome
        self.eta = eta

    def presentati(self):
        print(f"Mi chiamo {self.__nome} {self.cognome} {self.eta}")



ciccio = Persona("kjhglj","ciccio", "pasticcio",23)

#ciccio.presentati()