def main():
    id = list(input())
    print(scan(id, 0, 0), end='')

def scan(id, sum1, sum2):
    for i in range(len(id)//2):
        sum1 += int(id[i])
    for i in range(len(id)//2, len(id)):
        sum2 += int(id[i])
    return('FORTUNATO' if sum1 == sum2 else 'SFORTUNATO')
main()