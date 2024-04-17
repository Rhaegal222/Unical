def main():
    n = int(input())
    frase = list(input())
    for i in frase:
        if i == ' ':
            frase.remove(i)
    
    f1 = [frase[i] for i in range(n-1)]
    f2 = [frase[i] for i in range(n-1, len(frase))]

    f1 = sorting(f1)
    f2 = sorting(f2)
    
    print('SI' if ricorsiva(f1, f2, 0) else 'NO', end='')
    
def sorting(frase):
    for i in range(len(frase)-1):
        for j in range(len(frase)-1-i):
            if frase[j] > frase[j+1]:
                frase[j], frase[j+1] = frase[j+1], frase[j]
    return frase

def ricorsiva(f1, f2, i):
    if i >= len(f1):
        return True
    if len(f1) != len(f2):
        return False
    if f1[i] != f2[i]:
        return False
    return ricorsiva(f1, f2, i+1)
main()