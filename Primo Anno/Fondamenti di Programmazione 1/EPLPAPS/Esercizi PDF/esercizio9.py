def cerca_parola(prima, seconda, cont, contate):
    prima = prima.split(' ')
    seconda = seconda.split(' ')

    for i in prima:
        if i in seconda and i not in contate:
            cont += 1
            contate.append(i)
    return cont

print(cerca_parola(input(), input(), 0, []))