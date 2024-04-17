def main():
    anno = int(input())
    scanner(anno)

def scanner(anno):
    if anno % 100 == 0 and anno % 400 == 0:
        print('BISESTILE', end='')
    elif anno % 100 != 0 and anno % 4 == 0:
        print('BISESTILE', end='')
    else:
        print('NON BISESTILE', end='')
main()
