def main():
    n = int(input())
    nonogram = create(n, [])
    col = insert(n, [])
    row = insert(n, [])
    new_row = scan(nonogram, [])
    nonogram = inverter(nonogram)
    new_col = scan(nonogram, [])
    
    print('SI' if new_col == col and new_row == row else 'NO', end='')

def scan(nonogram, row):
    for i in nonogram:
        row.append(i.count(1))
    return row

def inverter(nonogram):
    empty = []
    for i in range(len(nonogram)):
        empty.append([])
        for j in range(len(nonogram)):
            empty[i].append(nonogram[j][i])
    return empty

def pr(nonogram):
    for i in range(len(nonogram)):
        for j in range(len(nonogram)):
            print(nonogram[i][j], '', end='')
        print()

def insert(n, seq):
    for i in range(n):
        seq.append(int(input()))
    return seq

def create(n, nonogram):
    for i in range(n):
        nonogram.append([])
        for j in range(n):
            nonogram[i].append(int(input()))
    return nonogram
main()