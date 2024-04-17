def ricorsiva(x):
    if x <= 0:
        return False
    elif x == 1:
        return True
    y = ((3*x)-2)//6
    if y <= 0:
        return False
    elif y == 1:
        return True
    elif y > 1:
        return ricorsiva(y)

print(ricorsiva(int(input())))
