def main():
    print(ricorsiva(int(input())), end='')

def ricorsiva(n):
    return 2 if n == 0 else 3*(n+1)*ricorsiva(n-1)
main()