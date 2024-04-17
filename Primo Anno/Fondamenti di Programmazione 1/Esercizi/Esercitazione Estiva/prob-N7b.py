def main():
    seq = inserimento()
    stampa(seq)

def inserimento():
    x = int(input())
    n = int(input())
    seq = []
    for i in range(n):
        g = int(input())
        if g < x and g % 2==0:
            seq.append(g)
    return seq

def stampa(seq):
    for i in seq:
        print(i, end='')
        
    
main()
