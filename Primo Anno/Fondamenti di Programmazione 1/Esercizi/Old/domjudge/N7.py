def main():
    print(fun_multiplo(False), end='')

def fun_multiplo(multiplo):
    n = int(input())
    if n != 5:
        if n % 5 == 0:
            multiplo = True
        return fun_multiplo(multiplo)
    else:
        if multiplo:
            return ('ALMENO 1')
        else:
            return ('NESSUNO')
main()