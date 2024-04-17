def main():
    results = insert([[], [], []])
    print(scan(results), end='')

def insert(lista):
    x = int(input())
    if x != 0:
        lista[x-1].append(x)
        return insert(lista)
    else:
        return lista

def scan(results):
    voti = 0
    percentuali = []
    
    for i in range(len(results)): voti += len(results[i]) 
        
    if voti > 0:    
        for i in range(len(results)):
            per = round((len(results[i])/voti)*100, 1)
            percentuali.append(per)
            print(i+1, len(results[i]), per)

        for i in range(len(percentuali)):
            if percentuali[i]> 50:
                return 'VINCE '+str(i+1)
    return('BALLOTTAGGIO')
main()