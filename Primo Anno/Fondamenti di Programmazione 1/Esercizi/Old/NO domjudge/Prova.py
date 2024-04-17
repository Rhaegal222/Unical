def main():
    N = int(input())
    Lista = crealista(N)
    stampa_lista(Lista)

def crealista(N):
    array = []
    for i in range(N):
        array.append(input())
    return array

def stampa_lista(Lista):
    Lista.sort(reverse=True)
    print(Lista)
    Lista.sort()
    print(Lista)

         
main()