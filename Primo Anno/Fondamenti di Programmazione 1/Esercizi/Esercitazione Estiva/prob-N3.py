import math
def main():
    A = int(input())
    scanner(A)

def scanner(A):
    if A%2==0:
        print('PARI', end='')
    else:
        print('DISPARI', end='')
main()