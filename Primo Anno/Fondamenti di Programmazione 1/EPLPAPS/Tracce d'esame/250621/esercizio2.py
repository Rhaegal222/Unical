def main():
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    ricorsiva(A, B, C, D, A, C)

def ricorsiva(A, B, C, D, i, j):
    if i > B:
        return
    else:
        x = i
        y = j
        if x < y:
            print(x, y)
            if j < D:
                return ricorsiva(A, B, C, D, i, j+1)
            else:
                return ricorsiva(A, B, C, D, i+1, C)
        else:
            return ricorsiva(A, B, C, D, i, j+1)

        
    
main()