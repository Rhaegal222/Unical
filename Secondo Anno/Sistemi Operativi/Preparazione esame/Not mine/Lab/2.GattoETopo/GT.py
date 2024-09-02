import random
from threading import Thread
from random import randint
'''class Striscia(Thread):
    def __init__(self)'''

def main():
    S=[]
    L=10
    for i in range(L): S.append(" ")
    SinToDes=True
    G=random.randint(0,L-1)
    T=random.randint(0,L-1)
    while(T==G): T=random.randint(0,L)
    S[G]="*"
    S[T]="."
    Display(S,L,G,T)
    while (G!=T):
        G,SinToDes=Gatto(S,L,G,SinToDes)
        T=Topo(S,L,T)
        Display(S,L,G,T)

def Display(S,L,G,T):
    if (G!=T):
        for i in range(L):print(S[i],end="")
    else: print(f"Il gatto ha raggiunto i l topo")
def Gatto(S,L,G,SinToDes):
    if(G==L-1): #se è alla fine stringa
        SinToDes=False
    if(G==0): #se è a inizio stringa
        SinToDes=True
    if(SinToDes):
        S[G]=" "
        G+=1 #incremento
        S[G]="*"
    else:
        S[G]=" "
        G-=1 #decremento
        S[G]="*"
    return G, SinToDes

def Topo(S,L,T):
    if(T>0 and T<L-1):
        S[T]=" "
        T+=random.randint(-1,1)
        S[T]="."
    elif(T==L-1): #se è alla fine stringa
        S[T]=" "
        T+=random.randint(-1,0)
        S[T]="."
    elif(T==0): #se è a inizio stringa
        S[T]=" "
        T+=random.randint(0,1)
        S[T]="."
        return T
main()
