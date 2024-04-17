N = int(input())

if N < 0:
    print("VOTO NON VALIDO", end="")
elif N > 30:
    print("VOTO NON VALIDO", end="")
elif N >= 18:
    print("ESAME SUPERATO", end="")
else:
    print("BOCCIATO", end="")


