import random
def crea_anagramma(prima_parola, backup_prima_parola):
    prima_parola = list(prima_parola)
    casuale = random.randint(0, len(prima_parola)-1)
    for i in range(casuale):
        for j in range(casuale):
            temp = prima_parola[i]
            prima_parola[i] = prima_parola[casuale]
            prima_parola[casuale] = temp
    nuova_parola = prima_parola
    if nuova_parola == list(backup_prima_parola):
        return crea_anagramma(prima_parola, prima_parola)
    else:
        print(''.join(nuova_parola))

def cerca_anagramma(prima_parola, seconda_parola):
    anagramma = ''
    for i in prima_parola:
        for j in seconda_parola:
            if i == j:
                anagramma += j
                break
    if prima_parola == anagramma:
        return True
    else:
        return False

def inserisci_parole():
    prima_parola = input()
    seconda_parola = input()
    return prima_parola, seconda_parola

def main():
    prima_parola, seconda_parola = inserisci_parole()
    if len(prima_parola) == len(seconda_parola):
        anagramma = cerca_anagramma(prima_parola, seconda_parola)
    else:
        anagramma = False
    if not(anagramma):
        anagramma = crea_anagramma(prima_parola, prima_parola)
    else:
        print(anagramma)
main()