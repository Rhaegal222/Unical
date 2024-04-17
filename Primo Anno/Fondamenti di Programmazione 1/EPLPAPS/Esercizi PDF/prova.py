a = list(input())
print(a)
stringa = 'oggi non si studia'
parola = ''
parole = []
for i in stringa:
    if i != ' ':
        parola += i
    else:
        parole.append(parola)
        parola = ''
parole.append(parola)
print(parole)
