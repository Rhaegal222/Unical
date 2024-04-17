A = -1
B = 0
S = 0
while True:
    A = int(input())
    if A == 0:
        break
    B = input()
    if B == 's':
        S = S + (A * 1)
    elif B == 'm':
        S = S + (A * 60)
    elif B == 'h':
        S = S + (A * 3600)
print(S, end="")