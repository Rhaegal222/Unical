import math
def main():
    A, B = inserimento()
    label = ['Somma:', 'Differenza:', 'Moltiplicazione:', 'Quoziente:', 'Resto:']
    operations = [A+B, A-B, A*B, A/B, A%B]
    calculating(A, B, label, operations, 0)

def inserimento():
    A = int(input())
    B = int(input())
    return A, B

def calculating(A, B, label, operations, i):
    print(label[i], math.trunc(operations[i]), end='')
    if i < 4:
        print()
        return calculating(A, B, label, operations, i+1)
main()