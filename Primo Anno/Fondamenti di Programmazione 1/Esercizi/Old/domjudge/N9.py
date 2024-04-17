N = int
i = 0
while N != 0:
    N = int(input())
    if N % 2 != 0 and N % 3 == 0:
        i = i + 1
print(i, end="")