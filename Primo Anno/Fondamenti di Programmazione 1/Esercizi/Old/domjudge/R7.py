def main():
    A = int(input())
    B = int(input())
    print(MCD(A, B), end='')
def MCD(A, B):
    if A == 0 or B == 0:
        return 0
    else:
        r = A%B
    if r == 0:
        return B
    return MCD(B, r)
main()