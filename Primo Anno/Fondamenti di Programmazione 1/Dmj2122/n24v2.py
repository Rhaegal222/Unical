def main():
    stringa = fun('')
    result = scan(stringa, 0)
    print(result, end='')

def scan(stringa, cont):
    vocali = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(stringa)):
        if i < len(stringa)-1:
            if stringa[i] in vocali and stringa[i+1] in vocali:
                cont += 1
            if not(stringa[i] in vocali) and not(stringa[i+1] in vocali):
                 cont +=1
        else:
            cont +=1
    return cont

def fun(stringa):
    x = input()
    if x == '.':
        return list(stringa)
    else:
        stringa += x
        return fun(stringa)

main()