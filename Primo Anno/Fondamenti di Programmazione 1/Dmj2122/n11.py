def main():
    n = int(input())
    print(scan(n), end='')

def scan(n):
    n = str(n)
    for i in n:
        if i == '0':
            return 'NO'
    return 'SI'

main()