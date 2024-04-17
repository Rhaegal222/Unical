def main():
    print('SI' if scan(False) else 'N0', end='')

def scan(cond):
    x = input()
    if x != '.':
        return(scan(True) if x.isalpha() else scan(cond))
    else:
        return(False)
main()
