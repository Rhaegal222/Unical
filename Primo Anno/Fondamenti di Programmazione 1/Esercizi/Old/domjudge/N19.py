N = 0
C = False
while N != '*':
    N = input()
    if N == "0" or N == "1" or N == "2" or N == "3" or N == "4" or N == "5" or N == "6" or N == "7" or N == "8" or N == "9":
        C = True
if C:
    print('ALMENO UNA', end="")
else:
    print('NESSUNA', end="")
