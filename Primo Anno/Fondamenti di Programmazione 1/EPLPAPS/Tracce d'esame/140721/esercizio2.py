def main():
    numero_brani = int(input())
    anno = int(input())
    tabella = [[int(input()) for j in range(2)] for i in range(numero_brani)]
    brani_max, no_rip = scan(tabella, anno)
    print(brani_max, 'SI' if no_rip else 'NO', end='')

def scan(tabella, anno):
    anni = []
    for i in tabella:
        anni.append(i[1])

    brani_max = anni.count(anni[0])

    for i in range(1, len(anni)):
        if anni.count(anni[i]) > anni.count(brani_max):
            brani_max = anni[i]
    
    no_rip = True

    for i in range(len(tabella)):
        if tabella[i][1] == anno and tabella[i][0] != 0:
            no_rip = False
            break

    return brani_max, no_rip

main()