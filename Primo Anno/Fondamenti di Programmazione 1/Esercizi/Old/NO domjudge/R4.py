X = int(input())
N = int(input())
lista = [int(input()) for x in range(N)]

def fun_rec(lista, x, i, nX):
    if i >= N and nX == 0:
        return 0

    if i >= N:
        return nX + fun_rec(lista,nX,0,0)

    if x == lista[i]:
        lista[i] = 0
        return fun_rec(lista,x,i+1,nX+1)

    return fun_rec(lista,x,i+1,nX)
 
print(fun_rec(lista,X,0,0),end="")