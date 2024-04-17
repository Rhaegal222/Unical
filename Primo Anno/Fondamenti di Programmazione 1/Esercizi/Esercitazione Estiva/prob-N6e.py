def main():
    Elementi = inserimento()
    ValoriCarte = {1: 11, 2: 2, 3: 10.5, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}
    Start(Elementi, ValoriCarte)

def inserimento():
    Elementi = []
    for i in range(5):
        Elementi.append(int(input()))
    return Elementi

def Start(Elementi, ValoriCarte):
    StessoSeme = Elementi[1] == Elementi[3]
    CartaMaggiore = ValoriCarte[Elementi[2]] > ValoriCarte[Elementi[4]]
    BriscolaPrimoGiocatore = Elementi[0] == Elementi[1]
    BriscolaSecondoGiocatore = Elementi[0] == Elementi[3]
    
    if(StessoSeme):
        if(CartaMaggiore):
            print("VINCE GIOCATORE 1",end="")
        else:
            print("VINCE GIOCATORE 2", end="")
    else:
        if(BriscolaPrimoGiocatore):
            print("VINCE GIOCATORE 1",end="")
        elif(BriscolaSecondoGiocatore):
            print("VINCE GIOCATORE 2", end="")
        else:
            print("VINCE GIOCATORE 1",end="")
main()
