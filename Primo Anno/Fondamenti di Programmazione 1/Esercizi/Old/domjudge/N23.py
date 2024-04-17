N = input()
C = False
while N != "*":
    if N == "a" or N == "e" or N == "i" or N == "o" or N == "u":
        C = True
    N = input()
if C == False:
    print("NESSUNA VOCALE",end="")
else:
    print("ALMENO 1 VOCALE",end="")