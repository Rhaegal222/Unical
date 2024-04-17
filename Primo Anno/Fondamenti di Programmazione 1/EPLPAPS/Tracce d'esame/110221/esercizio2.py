def ricorsiva(C, I, i, j, k):
    if k == len(I):
        return
    if i < len(C):
        if j < len(C):
            if i != j:
                print(str(I[k])+C[i]+C[j])
            return ricorsiva(C, I, i, j+1, k)
        else:
            return ricorsiva(C, I, i+1, 0, k)
    else:
        return ricorsiva(C, I, 0, 0, k+1)

I = [1, 13]
C = ['a', '*', 'w']
ricorsiva(C, I, 0, 0, 0)