def main():
    Calls = int(input())
    Price = calculating(Calls)

def calculating(Calls):
    if Calls <= 80:
        Price = 5
    elif Calls > 80 and Calls <= 140:
        Price = 5 + (Calls - 80)*0.10
    elif Calls > 140 and Calls <= 190:
        Price = 11 + (Calls - 140)*0.07
    else:
        Price = 14.5 + (Calls - 190)*0.05
    print(round(Price, 2), end = '')

main()
