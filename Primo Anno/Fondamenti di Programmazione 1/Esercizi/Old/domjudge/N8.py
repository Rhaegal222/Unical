x = int(input())
y = int(input())

tot = 0
y2 = y


while y2 >= x:
    if y2%2 != 0:
        tot +=y2
    y2 -= 1

print(tot, end="")
