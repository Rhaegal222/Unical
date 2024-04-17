N = int(input())
M = int(input())

i = 1
c = 0

while i <= N:
    a = N % i
    if a == 0:
       c = c + 1
    i = i + 1

i = 1
d = 0

x = abs(M-N)

while i <= M:
    b = M % i
    if b == 0:
       d = d + 1
    i = i + 1

if c > 2 and d > 2:
    print('non entrambi primi', end="")
elif c == 2 and d > 2:
    print('non entrambi primi', end="")
elif c > 2 and d == 2:
    print('non entrambi primi', end="")
elif c == 2 and d == 2 and x != 2:
    print('non gemelli', end="")
elif c == 2 and d == 2 and x == 2:
    print('gemelli', end="")
