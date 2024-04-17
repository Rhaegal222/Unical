def main():
    n_packs = int(input())
    pfp = [int(input()) for i in range(n_packs)]
    piv = []
    x = input()
    while x != '*':
        piv.append(int(x))
        x = input()
    processing(pfp, piv)

def processing(pfp, piv):
    for i in piv:
        if i in pfp:
            print(i)
            pfp.remove(i)
        else:
            pfp, combo = src_combo(i, pfp)
            if type(combo[0]) == int:
                print(combo[0], combo[1])
            elif type(combo[0]) == list:
                min = src_min(combo)
                print(min[0], min[1])
            else:
                print(combo)                
                
def src_min(combo):
    min = combo[0]
    for i in combo:
        if sum(i) < sum(min):
            min = i
    return min

def src_combo(piv, pfp):
    combo = []
    for i in range(len(pfp)):
        for j in range(len(pfp)):
            if i != j and pfp[i]+pfp[j] == piv:
                combo = [pfp[i], pfp[j]]
                pfp.pop(i)
                pfp.pop(j-1)
                return pfp, combo
    
    for i in range(len(pfp)):
        for j in range(len(pfp)):
            if i != j and pfp[i]+pfp[j] > piv:
                combo.append([pfp[i], pfp[j]])
    if combo != []:
        return pfp, combo
    else:
        return pfp, 'NO'
            
main()