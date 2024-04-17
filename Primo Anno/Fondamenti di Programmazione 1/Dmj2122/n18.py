x, temp, cont = input(), '', 1
while not(x=='k' and temp =='o'):
    temp, x, cont = x, input(), cont+1
print(cont-2, end='')