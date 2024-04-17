def search(numero):
    divisori = []
    for i in range(2 , numero-1):
        if numero % i == 0:
            divisori.append(i)
    return divisori

def NumeriFidanzati(A, B):
    for i in range(A, B+1):
        for j in range(A, B+1):
            if i != j:
                if sum(search(i)) == j and sum(search(j)) == i:
                    return True
    return False

def main():
    print('SI' if NumeriFidanzati(int(input()), int(input())) else 'NO', end='')

main()