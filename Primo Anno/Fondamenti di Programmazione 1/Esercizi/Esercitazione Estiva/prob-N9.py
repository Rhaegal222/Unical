cont = 0
while True:
    x = int(input())
    if x % 3 == 0 and x % 2 != 0:
        cont += 1
    if x == 0:
        break
print(cont, end='')
