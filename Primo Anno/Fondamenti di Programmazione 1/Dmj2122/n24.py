def main():
    stringa = fun('')
    result = scan(stringa, '', [])
    print(result, end='')

def scan(stringa, temp, sot):
    vocali = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(stringa)):
        temp += stringa[i]
        if i < len(stringa)-1:
            if stringa[i] in vocali and stringa[i+1] in vocali:
                sot.append(temp)
                temp = ''
            if not(stringa[i] in vocali) and not(stringa[i+1] in vocali):
                sot.append(temp)
                temp = ''
        else:
            sot.append(temp)
    return len(sot)

def fun(stringa):
    x = input()
    if x == '.':
        return list(stringa)
    else:
        stringa += x
        return fun(stringa)

main()