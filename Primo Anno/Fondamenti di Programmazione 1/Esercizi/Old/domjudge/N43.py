def parentesi(x):

    par = 0
    err1 = False
    err2 = False
    M = None

    for i in x:
        if i == '(':
            par += 1
        if i == ')':
            par -= 1
            if par < 0:
                err1 = True
            if M != None and M == '(':
                err2 = True
        M = i

    if par != 0:
        err1 = True

    if not err1:
        print("ok1")
    else:
        print("no1")
    if not err2:
        print("ok2")
    else:
        print("no2")
    
x = input()

parentesi(x)
