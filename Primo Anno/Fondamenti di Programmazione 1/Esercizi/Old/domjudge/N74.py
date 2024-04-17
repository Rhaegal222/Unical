def main():
    N = int(input())
    area = calcolo_area(N)
    print(round(area)+1, end='')

def diagonale(N):
    D = (N-1) + N
    return D

def calcolo_area(N):
    D = diagonale(N)
    Area = (D**2)/2
    return Area
main()