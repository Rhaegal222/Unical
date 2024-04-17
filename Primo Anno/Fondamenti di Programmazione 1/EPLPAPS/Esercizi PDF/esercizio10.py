def ricorsiva(A, B, C, i):
    if i >= 0:
        C.append(A[(len(B)-1) - i])
        C.append(B[i])
        return ricorsiva(A, B, C, i-1)
    return C

A = list(input())
B = list(input())
print(ricorsiva(A, B, [], len(B)-1))