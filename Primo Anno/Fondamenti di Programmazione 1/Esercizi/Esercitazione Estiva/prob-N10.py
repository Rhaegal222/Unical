n = input()
ninv = ''
for i in range(len(n)-1, -1, -1):
    ninv += n[i]
print(int(n) - (int(ninv)), end='')
    
