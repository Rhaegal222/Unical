N = int(input())
i = 1
c = 0
while i <= N:
    a = N % i
    if a == 0:
       c = c + 1
    i = i + 1
if c > 2:
    print('NO', end="")
else:
    print('SI', end="")




