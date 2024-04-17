def main():
    variabile = list(input())
    print('SI' if scan(variabile) else 'NO', end='')

def scan(variabile):
    for i in range(len(variabile)):
        if variabile[0].isdigit():
            return False
        if variabile[i] == ' ':
            return False
    return True        

main()