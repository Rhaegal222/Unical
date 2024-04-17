def main():
    voto_conseguito = int(input())
    esito(voto_conseguito)

def esito(voto_conseguito):
    if voto_conseguito < 0 or voto_conseguito > 30:
        print('VOTO NON VALIDO', end = '')
    elif voto_conseguito >= 18:
        print('ESAME SUPERATO', end = '')
    else:
        print('BOCCIATO', end = '')

main()
        
