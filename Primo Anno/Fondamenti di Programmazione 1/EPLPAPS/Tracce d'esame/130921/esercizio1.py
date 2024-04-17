def main():
    print(arabo_romano(int(input())), end='')
    
def arabo_romano(numero):
    m = ["", "M", "MM", "MMM"]
    c = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    d = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    u = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    qm = int(numero / 1000) # migliaia
    qc = int((numero - qm * 1000) / 100) # centinaia
    qd = int((numero - qm * 1000 - qc * 100) / 10) # decine
    qu = int(numero - qm * 1000 - qc * 100 - qd * 10) # unità
    mm = m[qm]
    cc = c[qc]
    dd = d[qd]
    uu = u[qu]
    return (mm + cc + dd + uu)
main()