cont = 0
a = 0
e = 0
i = 0
o = 0
u = 0
while cont != 100:
    x = input()
    cont += 1
    if a < 1 and x == "a":
        a = 1
    if e < 1 and x == "e":
        e = 1
    if i < 1 and x == "i":
        i = 1
    if o < 1 and x == "o":
        o = 1
    if u < 1 and x == "u":
        u = 1
Somma = a + e + i + o + u
if Somma < 2:
    print("OK", end="")
else:
    print("ERRORE", end="")