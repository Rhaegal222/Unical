def main():
    total_amount = 500.0
    mesi = ['PRIMO', 'SECONDO', 'TERZO']
    operations(total_amount, 0, mesi)
def operations(total_amount, i, mesi):
    if i >= 1:
        total_amount -= 5.0
        total_amount *= 1.02
    print(mesi[i], 'MESE:', round(total_amount), end='')
    if i < 2:
        print()
        return operations(total_amount, i+1, mesi)
main()