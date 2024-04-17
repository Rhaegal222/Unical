a = 0
b = 0
Reparto1 = 0
Reparto2 = 5

while True:
    a = int(input("Digitare 1 per fumatori o 2 per non fumatori:"))
    if a == 1:
        if Reparto1 > 4:
            b = input("Reparto scelto al completo. Si desidera un posto nell'altro reparto (S/N)?")
            if b == 'S':
                if Reparto2 > 9:
                    print("Il prossimo volo parte tra 3 ore")
                else:
                    Reparto2 += 1
                    print("Reparto NON fumatori, posto", Reparto2)                    
            else:
                print("Il prossimo volo parte tra 3 ore")
        else:
            Reparto1 += 1
            print("Reparto fumatori, posto", Reparto1)
            
            

    if a == 2:
        if Reparto2 > 9:
            b = input("Reparto scelto al completo. Si desidera un posto nell'altro reparto (S/N)?")
            if b == 'S':
                if Reparto1 > 4:
                    print("Il prossimo volo parte tra 3 ore")
                else:
                    Reparto1 += 1
                    print("Reparto fumatori, posto", Reparto1)
                    
            else:
                print("Il prossimo volo parte tra 3 ore")
        else:
            Reparto2 += 1
            print("Reparto NON fumatori, posto", Reparto2)
            

    if Reparto1 + Reparto2 > 14:
        break
