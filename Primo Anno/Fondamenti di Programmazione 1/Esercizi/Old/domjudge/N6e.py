ValoriCarte = {1: 11, 2: 2, 3: 10.5, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10}

SemeBriscola = int(input())

SemePrimoGiocatore = int(input())
CartaPrimoGiocatore = int(input())

SemeSecondoGiocatore = int(input())
CartaSecondoGiocatore = int(input())

BriscolaPrimoGiocatore = (SemePrimoGiocatore == SemeBriscola)
BriscolaSecondoGiocatore = (SemeSecondoGiocatore == SemeBriscola)

CartaMaggiore = (ValoriCarte[CartaPrimoGiocatore] > ValoriCarte[CartaSecondoGiocatore])
StessoSeme = (SemePrimoGiocatore == SemeSecondoGiocatore)

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