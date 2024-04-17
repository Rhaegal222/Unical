def main():
    x = int(input())
    print(scan(str(x)), end='')

def scan(x):
    for i in x:
        if i == '0':
            return 'NO'
    return 'SI'
main()