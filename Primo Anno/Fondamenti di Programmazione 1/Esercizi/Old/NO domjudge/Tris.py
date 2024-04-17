P1 = input("Name's Player 1: ")
P2 = input("Name's Player 2: ")

S = input('X o O '+ P1 + ' fai la tua scelta: ')

if S == 'X':
    P1S = 'X'
    P2S = 'O'
    print(P1, 'ha scelto X', P2, 'ha scelto O')
else:
    P1S = 'O'
    P2S = 'X'
    print(P2, 'ha scelto X', P1, 'ha scelto O')

Table = []

print('Per giocare inserisci le coordinate della casella')
print('Le caselle sono numerate da 1 a 9 partendo dalla prima in alto a sinistra')

if P1S == 'X':
    print(P1, 'fa la prima mossa')
    Primo = P1
    Secondo = P2

elif P2S == 'X':
    print(P2, 'fa la prima mossa')
    Primo = P2
    Secondo = P1

for i in range(3):
    Table.append([])
    for j in range(3):
        Table[i].append('')

print(Table)
cont = 0
cont2 = 0

while True:
    
    print(Primo, end='') 
    Giocata1 = int(input(' Fai al tua giocata: '))-1 
    cont += 1

    for i in range(3):
        for j in range(3):
            if Giocata1 == i*3+j:
                if Table[i][j] != P1S and Table[i][j] != P2S:
                        Table[i][j] = P1S
                        break
                else:
                    print('Non fare il furbetto la casella è occupata')
    
    if cont < 9:
        print(Secondo, end='') 
        Giocata2 = int(input(' Fai al tua giocata: '))-1
        cont += 1

    for i in range(3):
        for j in range(3):
            if Giocata2 == i*3+j:
                if Table[i][j] != P1S and Table[i][j] != P2S:
                    Table[i][j] = P2S
                    break
                else:
                    print('Non fare il furbetto la casella è occupata')
    
    if cont > 5:
        if Table[0][0] == Table[1][1] and Table[0][0] == Table[2][2]:
            if Table[0][0] == 'O':
                print('Vince O')
                break
            if Table[0][0] == 'X':
                print('Vince X')
                break

        if Table[0][2] == Table[1][1] and Table[0][2] ==  Table[2][0]:
            if Table[0][2] == 'O':
                print('Vince O')
                break
            if Table[0][2] == 'X':
                print('Vince X')
                break

        if Table[0][0] == Table[0][1] and Table[0][0] == Table[0][2]:
            if Table[0][0] == 'O':
                print('Vince O')
                break
            if Table[0][0] == 'X':
                print('Vince X')
                break

        if Table[1][0] == Table[1][1] and Table[1][0] == Table[1][2]:
            if Table[1][0] == 'O':
                print('Vince O')
                break
            if Table[1][0] == 'X':
                print('Vince X')
                break

        if Table[2][0] == Table[2][1] and Table[2][0] == Table[2][2]:
            if Table[2][0] == 'O':
                print('Vince O')
                break
            if Table[2][0] == 'X':
                print('Vince X')
                break

        if Table[0][0] == Table[1][0] and Table[0][0] == Table[2][0]:
            if Table[0][0] == 'O':
                print('Vince O')
                break

            if Table[0][0] == 'X':
                print('Vince X')
                break

        if Table[0][1] == Table[1][1] and Table[0][1] == Table[2][1]:
            if Table[0][0] == 'O':
                print('Vince O')
                break

            if Table[0][0] == 'X':
                print('Vince X')
                break

        if Table[0][2] == Table[1][2] and Table[0][2] == Table[2][2]:
            if Table[0][0] == 'O':
                print('Vince O')
                break

            if Table[0][0] == 'X':
                print('Vince X')
                break
        
        if cont > 9:
            break

    for i in range(3):
        for j in range(3):
            print(Table[i][j], end='')
        print('')

    print(Table)

for i in range(3):
        for j in range(3):
            print(Table[i][j], end='')
        print('')