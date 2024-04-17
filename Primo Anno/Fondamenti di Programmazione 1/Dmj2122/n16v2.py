def main():
    x = int(input())
    print('OK' if scan(x, 0) else 'NO', end='')

def scan(x, count):
    n = int(input())
    if n != -1:
        if count < x:
            return(scan(x, count+1) if n == 0 else scan(x, 0))
        else:
            return scan(x, count)
    else:
        return (True if count >= x else False)
main()