def main():
    x = int(input())
    n = int(input())
    l = [int(input()) for i in range(n)]
    print(ricorsiva(x, l), end='')

def ricorsiva(x, l):
    c = 0
    if x == 0:
        return 0
    for i in range(len(l)):
        if l[i] == x:
            l[i] = 0
            c += 1
    return c+ricorsiva(c, l)
main()