stringa = input()
condizione = False
for i in stringa:
    if i == ' ' or not(i == '_' or i.isalnum()):
        condizione = True
if stringa[0].isdigit():
    condizione = True
if condizione:
    print('NO', end="")
else:
    print('SI', end="")