e=[]
g=[]
for i in range(10):
    e.append(int(input()))
for i in range(10):
    g.append(int(input()))
l=0
lmax=0
for gin in range(10):
    while (gin+l<len(g) and g[gin+l] in e):
        l+=1
        if (l>lmax):
            lmax=l
            l=0

if (lmax>1 and lmax<5):
    print(lmax, end='')
elif (lmax >=5):
    print(5, end='')
else:
    print(0, end='')

