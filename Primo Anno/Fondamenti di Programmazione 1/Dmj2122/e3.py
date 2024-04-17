def main():
    sequenza = inserimento([], input())
    sotto_seq = split(sequenza, [[]], 0)
    print(search(sotto_seq, []), end='')

def inserimento(sequenza, x):
    while x != '*':
        sequenza.append(int(x))
        x = input()
    return sequenza

def split(sequenza, sotto_seq, puntatore):
    for i in range(len(sequenza)-1):
        if sequenza[i] != sequenza[i+1]-1:
            sotto_seq[puntatore].append(sequenza[i])
            sotto_seq.append([])
            puntatore += 1
        else:
            sotto_seq[puntatore].append(sequenza[i])
    sotto_seq[puntatore].append(sequenza[i+1])
    return sotto_seq

def search(sotto_seq, max_seq):
    for i in sotto_seq:
        if len(i) > 1:
            max_seq.append(i)
    return len(max_seq)

main()