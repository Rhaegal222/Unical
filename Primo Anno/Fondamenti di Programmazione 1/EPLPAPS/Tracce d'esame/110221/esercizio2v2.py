I = [1, 13]
C = ['a', '*', 'w']

for i in range(len(I)):
    for j in range(len(C)):
        for k in range(len(C)):
            if i != j:
                print(str(I[i])+C[j]+C[k])