def ricorsiva(N):
    if N == 0:
        return 2
    else:
        return 3 * (N+1) * ricorsiva (N-1)

N = int(input())

print(ricorsiva(N), end='')
