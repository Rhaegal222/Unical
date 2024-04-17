def main():
    cond1, cond2 = scan(list(input()), False, True, 0, 0)
    print('ok1' if cond1 else 'no1')
    print('ok2' if cond2 else 'no2', end='')

def scan(stringa, cond1, cond2, count1, count2):
    for i in range(len(stringa)):
        if stringa[i] == '(':
            count1 += 1
        elif stringa[i] == ')':
            count2 += 1
    
    for i in range(len(stringa)-1):
        if stringa[i] == '(' and stringa[i+1] == ')':
            cond2 = False
            break
        if stringa[i] == ')' and stringa[i+1] == '(':
            cond2 = False
            break
        
    if count1 == count2:
        cond1 = True
    
    return cond1, cond2

main()