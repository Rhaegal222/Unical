def main():
    seq = insert([], input())
    if len(seq)>2:
        sub_seq = src_sub_seq(seq, [[]], 0)
        sub_seq_max = src_sub_seq_max(sub_seq, sub_seq[0])
        sub_seq_max = result(sub_seq_max, 0)
    else:
        sub_seq_max = 0
    print(sub_seq_max, end='')

def result(sub_seq_max, count):
    end = sub_seq_max[0]
    start = sub_seq_max[len(sub_seq_max)-1]
    for i in range(ord(start)+1, ord(end)):
        count += 1
    return count

def src_sub_seq_max(sub_seq, sub_seq_max):
    for i in sub_seq:
        if len(i) > len(sub_seq_max):
            sub_seq_max = i
    return sub_seq_max

def src_sub_seq(seq, sub_seq, point):
    for i in range(len(seq)-1):
        if seq[i] >= seq[i+1]:
            sub_seq[point].append(seq[i])
        else:
            sub_seq[point].append(seq[i])
            sub_seq.append([])
            point += 1
    if i < len(seq): 
        sub_seq[point].append(seq[i+1])
    return sub_seq

def insert(seq, x):
    while x != '*':
        seq.append(x)
        x = input()
    return seq

main()