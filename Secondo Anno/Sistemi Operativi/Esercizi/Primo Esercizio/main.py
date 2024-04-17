from Persona import Persona
from Studente import Studente
from Esame import Esame

if __name__ == "__main__":

    # Costruttore di Studente
    francesco = Studente(cf="pcnfnc93b06d086o", nome="Francesco", cognome="Pacenza", eta=27, matricola=182452)

    # Stampa utilizzando il metodo ridefinito (override) dalla classe Studente
    francesco.print()

    print("")

    # Aggiunge un esame
    francesco.addEsame(Esame("ING", 6, 18))

    # Stampa la lista degli esami
    francesco.printListaEsami()

    print("")

    # "%.2f" tronca il numero float a 2 cifre decimali
    print ("La media ponderata è: %.2f" % (francesco.calcolaMedia()))

    # Ricerca un esame in carriera
    if francesco.controllaEsame(Esame("SOR", 12)):
        print ("L'esame è presente in carriera")
    else:
        print ("L'esame NON è presente in carriera")