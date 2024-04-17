X = int(input())
N = 0

zero_consecutivi = 0
max_zero_consecutivi = 0

while N != -1:
    N = int(input())
    if N == 0:
        zero_consecutivi += 1
        if zero_consecutivi > max_zero_consecutivi:
            max_zero_consecutivi = zero_consecutivi
    else:
        zero_consecutivi = 0

print("OK" if max_zero_consecutivi >= X else "NO", end="")
