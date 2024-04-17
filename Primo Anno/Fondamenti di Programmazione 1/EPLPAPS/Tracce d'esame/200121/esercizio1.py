def main():
    numero = int(input())
    divisori = search(numero, [])
    if len(divisori) in divisori:
        print('SI', end='')
    else:
        print('NO', end='')

def search(numero, divisori):
    for i in range(1, numero+1):
        if numero % i == 0:
            divisori.append(i)
    return divisori

main()