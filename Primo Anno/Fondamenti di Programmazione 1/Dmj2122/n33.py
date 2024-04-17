import random
random.seed(0)

def main():
    elements = ['sasso', 'carta', 'forbice']
    res_type = ['Pari:', 'Vinci tu:', 'Vince il PC:']
    final = ['Hai vinto la sfida!', 'Il PC ha vinto la sfida!']
    print(final[start(elements, res_type, 0, 0)])

def start(elements, res_type, contp1, contnpc):    
    p1 = giocata()
    print('hai giocato', elements[p1-1])
    
    npc = random.randint(1, 3)
    print('il PC ha giocato', elements[npc-1])
    
    results = scan(p1, npc)
    contp1, contnpc = calculating(results, contp1, contnpc)
    
    print(res_type[results])
    print(contp1,'-', contnpc, sep='')

    if contp1 < 3 and contnpc < 3:
        return start(elements, res_type, contp1, contnpc)
    else:
        return(0 if contp1 > contnpc else 1)

def giocata():
    p1 = int(input('Inserisci la giocata del primo giocatore (1: sasso, 2: carta, 3: forbice):'))
    return (p1 if p1 >= 1 and p1<=3 else giocata())

def scan(p1, npc):
    if p1 == npc: return 0
    elif npc == 3 and p1 == 1: p1 = 10
    elif npc == 1 and p1 == 3: npc = 10
    return(1 if p1 > npc else 2)

def calculating(results, contp1, contnpc):
    if results == 1: contp1 += 1
    elif results == 2: contnpc += 1
    return contp1, contnpc

main()