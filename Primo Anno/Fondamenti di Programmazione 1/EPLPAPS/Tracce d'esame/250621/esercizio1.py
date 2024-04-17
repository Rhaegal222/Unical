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
            if combo == 'NO':
                print(combo)
            else:
                print(combo[0], combo[1])

def src_combo(piv, pfp):
    combo = []
    for i in range(len(pfp)):
        for j in range(len(pfp)):
            if i != j and pfp[i]+pfp[j] == piv:
                combo = [pfp[i], pfp[j]]
                pfp.pop(i)
                pfp.pop(j-1)
                return pfp, combo
    combo = 'NO'
    return pfp, combo
            
main()