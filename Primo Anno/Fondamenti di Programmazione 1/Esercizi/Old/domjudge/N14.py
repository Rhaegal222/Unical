n = int
m = ''
e = 0
while n != -1:
    n = int(input())
    if n != -1 and n <= 9:
        m = m + str(n)
    elif n > 9:
        e = e + 1
if e > 0:
    print('ERRORE', sep="", end="")
elif m == '':
    print('VUOTO', sep="", end="")
elif int(m) % 3 == 0:
    print(m,'\nSI', sep="", end="")
else:
    print(m,'\nNO', sep="", end="")
