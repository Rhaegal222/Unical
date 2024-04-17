def main():
    x=int(input())
    L=leggiL(x)
    if len(L)<3:
        print("NO",end="")
    else:
        c=crescente(L)
        if c[0]==False and  c[1]==True:
            print("SI",end="")
        else:
            print("NO",end="")


def leggiL(x):
    L=[]
    while x!= 0:
        L.append(x)
        x=int(input())
    return L


def crescente(L):
    crescente=True
    
    for i in range (len(L)-1):
        if L[i]>=L[i+1]:
            crescente=False
            return decrescente(i+1,L,crescente, False)
    return (True,False)


def decrescente(i,L,crescente, decrescente):    
    for j in range (i,len(L)-1):
        if L[j]<=L[j+1]:
            crescente = True
            break
        else:
            decrescente = True

    return (crescente, decrescente)

main()