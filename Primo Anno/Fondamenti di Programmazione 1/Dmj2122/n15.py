def main():
    sequenza = inserimento(0, None, 0)
    print(sequenza, end='')

def inserimento(total, temp, count):
    x = int(input())
    count += 1
    if x == temp:
        if count > 2:
            if x == 9:
                return total
            else:
                return inserimento(total+1, x, count+1)
        else:
            return inserimento(total, x, count)
    else:
        return inserimento(total, x, 1)
main()