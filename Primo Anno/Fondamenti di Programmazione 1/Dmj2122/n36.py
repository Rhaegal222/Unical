lista = []
cond = False

l = int(input())

while(len(lista))<10:
    lista.append(l)
    if len(lista) < 10:
        l = int(input())

#for i in range(10):
#    lista.append(int(input()))

x = int(input())

for i in lista:
    if i%x==0:
        cond = True

if cond: print("NO", end="")
else: print("OK", end="")
