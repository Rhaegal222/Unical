Anno = int(input())
if Anno % 400 == 0:
    print("BISESTILE", end="")
elif Anno % 4 == 0 and Anno % 100 != 0:
    print("BISESTILE", end="")
else:
    print("NON BISESTILE", end="")

