X = int(input())
N = int(input())
i = 1
B = ''
while i <= N:
    A = int(input())
    i = i + 1
    if A % 2 == 0 and A < X:
        B = B + str(A)
print(B, end="")

