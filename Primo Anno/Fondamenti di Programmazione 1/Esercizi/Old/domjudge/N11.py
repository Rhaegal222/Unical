N = input()
l = (len(N))
N = int(N)
zero = False
while l > 0:
    a = N % 10
    if a == 0:
        zero = True
    N = N // 10
    l = l - 1
if zero:
    print('NO', end="")
else:
    print('SI', end="")

