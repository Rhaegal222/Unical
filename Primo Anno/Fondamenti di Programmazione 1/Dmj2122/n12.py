def main():
    n = int(input())
    print(scan(n), end='')

def scan(n):
    cont = 0
    for i in range(1,n+1):
        if n % i == 0:
            cont += 1
        if cont > 2:
          return 'NO'
    return 'SI'


main()