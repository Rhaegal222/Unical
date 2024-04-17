def main():
    sequenza = inserimento([], input())
    if len(sequenza) > 0:
        sotto_seq = scan(sequenza, [[]], 0)
        print(results(sotto_seq, 0), end='')
    else:
        print(0, end='')

def inserimento(lista, x):
    while x != '*':
        lista.append(int(x))
        x = input()
    return lista

def scan(sequenza, sotto_seq, cont):
    for i in range(len(sequenza)-1):
        if sequenza[i] != sequenza[i+1]-1:
            sotto_seq[cont].append(sequenza[i])
            sotto_seq.append([])
            cont += 1
        else:
            sotto_seq[cont].append(sequenza[i])
    if i < len(sequenza): sotto_seq[cont].append(sequenza[i+1])
    
    return sotto_seq

def results(sotto_seq, cont):
    for i in sotto_seq:
        if len(i) >= 2:
            cont += 1
    return cont




main()