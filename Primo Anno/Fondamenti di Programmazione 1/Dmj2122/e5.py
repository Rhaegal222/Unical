def main():
    sequenza = inserimento([], input())
    if len(sequenza) > 2:
        sotto_seq = scan(sequenza, [[]], 0)
        seq_max = sotto_seq_max(sotto_seq, sotto_seq[0])
        print(results(seq_max, 0), end='')
    else:
        print(0, end='')

def inserimento(lista, x):
    while x != '*':
        lista.append(x)
        x = input()
    return lista

def scan(sequenza, sotto_seq, cont):
    for i in range(len(sequenza)-1):
        if sequenza[i] < sequenza[i+1]:
            sotto_seq[cont].append(sequenza[i])
            sotto_seq.append([])
            cont += 1
        else:
            sotto_seq[cont].append(sequenza[i])
    if i < len(sequenza): 
        sotto_seq[cont].append(sequenza[i+1])
    
    return sotto_seq

def sotto_seq_max(sotto_seq, temp):
    for i in sotto_seq:
        if len(i) >= len(temp):
            temp = i
    return temp

def results(seq_max, cont):
    inizio = seq_max[len(seq_max)-1]
    fine = seq_max[0]
    for i in range(ord(inizio)+1, ord(fine)):
        cont += 1
    return cont

main()