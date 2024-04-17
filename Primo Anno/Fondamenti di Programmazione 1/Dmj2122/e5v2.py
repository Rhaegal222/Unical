sequenza = []
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
x = input()

while x != '*':
    sequenza.append(x)
    x = input()

if len(sequenza) > 1:
    sotto_seq = [[]]
    punta = 0

    for i in range(len(sequenza)-1):
        if sequenza[i] >= sequenza[i+1]:
            sotto_seq[punta].append(sequenza[i])
        else:
            sotto_seq[punta].append(sequenza[i])
            sotto_seq.append([])
            punta += 1
    if i < len(sequenza):
        sotto_seq[punta].append(sequenza[i+1])
        
    sotto_seq_max = sotto_seq[0]

    for i in sotto_seq:
        if len(i) > len(sotto_seq_max):
            sotto_seq_max = i

    cont = 0

    for i in alfabeto:
        if i < sotto_seq_max[0] and i > sotto_seq_max[len(sotto_seq_max)-1]:
            cont += 1

    print(cont, end='')
else:
    print(0, end='')
