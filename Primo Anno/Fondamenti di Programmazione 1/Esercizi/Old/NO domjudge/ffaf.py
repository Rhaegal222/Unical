from random import shuffle
lista = []
x = int(input())

for i in range(x):
    lista.append(i)
shuffle(lista)
print(lista)
for i in range(len(lista)-1):
    if (lista[i] + lista[i+1])%2==0:
        print(lista[i], lista[i+1])
