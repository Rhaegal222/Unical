def main():
    numero_brani = int(input())
    confronto = int(input())
    tabella, anni = inserimento(numero_brani, [], [])
    anno, esito = (scan(tabella, numero_brani, confronto, anni))
    print(anno, 'NO' if esito else 'SI', end='')

def inserimento(numero_brani, tabella, anni):
    for i in range(numero_brani):
        tabella.append([])
        play = int(input())
        anno = int(input())
        tabella[i].append(play)
        tabella[i].append(anno)
        if anno in anni:
            continue
        else:
            anni.append(anno)
    return tabella, anni

def scan(tabella, numero_brani, confronto, anni):
    brani_per_anno = []
    for i in range(len(anni)):
        brani_per_anno.append(0)
    
    anno = check1(tabella, numero_brani, anni, brani_per_anno, 0)
    
    esito = check2(tabella, numero_brani, confronto)

    return anno, esito

def check2(tabella, numero_brani, confronto):
    for i in range(numero_brani):
        if tabella[i][1] == confronto and tabella[i][0] > 0:
            return True
    return False

def check1(tabella, numero_brani, anni, brani_per_anno, cont):
    for i in anni:
        for j in range(numero_brani):
            if tabella[j][1] == i:
                brani_per_anno[cont] += 1
        cont += 1

    indice = 0
    
    for i in range(len(brani_per_anno)):
        if brani_per_anno[i] > brani_per_anno[indice]:
            indice = i
    
    return anni[indice]

main()