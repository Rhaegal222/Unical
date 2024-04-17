class Persona:
    # NON è POSSIBILE DEFINIRE PIù COSTRUTTORI
    # Costruttore con kwargs (keyword arguments)
    def __init__(self, **kwargs):
        if 'cf' in kwargs:
            self.cf = kwargs['cf']
        if 'nome' in kwargs:
            self.nome = kwargs['nome']
        if 'cognome' in kwargs:
            self.cognome = kwargs['cognome']
        if 'eta' in kwargs:
            self.eta = kwargs['eta']

    def _protectedMethod(self):
        print ("Metodo Protetto")

    def __privateMethod(self):
        print ("Metodo Privato")

# Costruttore con parametri di default
#    def __init__(self, cf="", nome="", cognome="", eta=0):
#        self.cf=cf
#        self.nome=nome
#        self.cognome=cognome
#        self.eta=eta

    def print(self):
        print ("Codice Fiscale:\t %s\nNome:\t\t %s\nCognome:\t %s\nEtà:\t\t %d" % (self.cf, self.nome, self.cognome, self.eta))

