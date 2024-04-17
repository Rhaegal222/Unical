def InputStringa():
    stringa = ''
    x = 0
    while x != '.':
        x = input()
        if x != '.':
            stringa = stringa + x
    return stringa    

stringa1, stringa2 = InputStringa(), InputStringa()

Stop = False
Output = 0
for c in stringa1:
    if Stop == True:
        break
    for c1 in stringa2:
        if c == c1:
            Output = c
            Stop = True
            break

if Output != 0:
    print(Output, end='')
else:
    print('DISGIUNTE', end='')
