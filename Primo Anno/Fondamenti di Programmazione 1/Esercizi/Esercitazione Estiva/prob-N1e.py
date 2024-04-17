def main():
    balance, fees, interest = inserimento()
    months = ['PRIMO', 'SECONDO', 'TERZO']
    operations(balance, fees, interest, months, 0)

def inserimento():
    balance = int(input())
    fees = int(input())
    interest = int(input())
    return balance, fees, interest

def operations(balance, fees, interest, months, i):
    if i >= 1:
        balance -= fees
        balance *= ((interest+100)/100)
    print(months[i], 'MESE:', round(balance), end='')
    if i < 2:
        print()
        return operations(balance, fees, interest, months, i+1)
main()