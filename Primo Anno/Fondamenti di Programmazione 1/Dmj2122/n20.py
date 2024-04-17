def main():
    print(scan(True), end='')

def scan(cond):
    x = input()
    if x == '.':
        return ('SI' if cond else 'NO')
    if x.isalpha() and cond:
        return scan(True)
    else:
        return scan(False)