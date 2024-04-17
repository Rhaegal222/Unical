def main():
    A, B = inserimento()
    label = ['AREA:', 'PERIMETRO:']
    operations = [A*B, (A*2)+(B*2)]
    calculating(A, B, label, operations, 0)

def inserimento():
    A = int(input())
    B = int(input())
    return A, B

def calculating(A, B, label, operations, i):
    print(label[i], operations[i], end='')
    if i < 1:
        print()
        return calculating(A, B, label, operations, i+1)
main()