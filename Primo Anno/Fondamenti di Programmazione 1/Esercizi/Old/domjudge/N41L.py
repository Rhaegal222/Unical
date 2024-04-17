L = []

a = 0
b = 0

postiLiberi = True

for i in range(10):
    L.append(0)

while postiLiberi:
    a = int(input("Digitare 1 per fumatori o 2 per non fumatori:"))

    Assign1 = False
    Assign2 = False
        
    if a == 1:
        for i in range(5):
            if L[i] == 0:
                L[i] = 1
                print("Reparto fumatori, posto", i+1)
                Assign1 = True
                break
                
        if not Assign1:
            b = input("Reparto scelto al completo. Si desidera un posto nell'altro reparto (S/N)?")
            if b == 'N':
                print("Il prossimo volo parte tra 3 ore")
            else:
                for i in range(5,10):
                    if L[i] == 0:
                        Assign2 = True
                        L[i] = 1
                        print("Reparto fumatori, posto", i+1)
                        break
                    
                if not Assign2:
                    postiLiberi = False
                    continue
            
    if a == 2:
        for i in range(5, 10):
            if L[i] == 0:
                L[i] = 1
                print("Reparto fumatori, posto", i+1)
                Assign2 = True
                break

        if not Assign2:
            b = input("Reparto scelto al completo. Si desidera un posto nell'altro reparto (S/N)?")
            if b == 'N':
                print("Il prossimo volo parte tra 3 ore")
            else:
                for i in range(5):
                    if L[i] == 0:
                        Assign1 = True
                        L[i] = 1
                        print("Reparto fumatori, posto", i+1)
                        break
                    
                if not Assign1:
                    postiLiberi = False
                    continue
                    
    postiLiberi = False
    for i in range(0, 10):
        if L[i] == 0:
            postiLiberi = True
            break
                
                
        
            
                    
                
        
    
