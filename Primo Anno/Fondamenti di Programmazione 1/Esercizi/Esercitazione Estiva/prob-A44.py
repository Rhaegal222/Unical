def main():
    number_id = list(input())
    validation_ticket(number_id)
def validation_ticket(number_id):
    sum1 = 0
    sum2 = 0
    for i in range(((len(number_id))//2)):
        sum1 = sum1 + int(number_id[i])
    for i in range((len(number_id)//2), len(number_id)):
        sum2 = sum2 + int(number_id[i])
    if sum1 == sum2:
        print('FORTUNATO', end='')
    else:
        print('SFORTUNATO', end='')
main()