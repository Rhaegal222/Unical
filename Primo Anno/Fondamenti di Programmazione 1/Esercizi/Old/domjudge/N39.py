import math
N = -1
Condition = True
while N != 0:
    N = int(input())
    if N == 0:
        break
    X = math.log2(N)
    if X % int(X) != 0:
        Condition = False
if Condition:
    print('SI', end="")
else:
    print('NO', end="")
