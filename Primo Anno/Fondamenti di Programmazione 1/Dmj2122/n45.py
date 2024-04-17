N = list(input())

for i in range(len(N)-1):
    for j in range(len(N)-1):
        if N[j] < N[j+1]:
            N[j], N[j+1] = N[j+1], N[j]

nmax = ''
for i in N:
    nmax += i

for i in range(len(N)-1):
    for j in range(len(N)-1):
        if N[j] > N[j+1]:
            N[j], N[j+1] = N[j+1], N[j]

nmin = ''
for i in N:
    nmin += i

nmax = int(nmax)
nmin = int(nmin)

print(nmax-nmin, end='')