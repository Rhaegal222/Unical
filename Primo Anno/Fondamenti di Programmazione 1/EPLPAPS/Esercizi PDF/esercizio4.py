def main():
    mail = [(input()).split(' ') for i in range(10)]
    cont1, cont2 = scan(mail, 0, 0)
    print(cont1, cont2)

def scan(mail, cont, cont2):
    words = ['amore', 'tesoro', 'cucciolotto', 'trottolino']
    words2 = ['amore', 'bacio', 'moglie']
    
    for i in mail:
        for j in i:
            if j in words:
                cont += 1
                break
    
    for i in mail:
        if (words2[0] in i) and (words2[1] in i) and (words2[2] not in i):
            cont2 += 1
    
    return cont, cont2
main()