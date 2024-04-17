def main():
    A = input().split(' ')
    B = [int(input()) for i in range(len(A))]
    print(scan(A, B, 0))

def scan(A, B, i):
    if i >= len(A):
        return True
    elif len(A[i]) != B[i]:
        return False
    else:
        return scan(A, B, i+1)
main()