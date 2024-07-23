t = int(input())

answers = []
for _ in range(t):
    n = int(input())
    bn = bin(n)[2:]
    reverse_bn = bn[::-1]
    bn_lst = [int(c) for c in reverse_bn]

    length = len(bn_lst)

    i = 0
    j = 0
    while (i < length and j < length+1):
        if bn_lst[i] == 0:
            i += 1
            j = i
        else:
            while j<length and bn_lst[j] == 1:
                    j += 1
            if j-i > 1:
                bn_lst[i] = -1
                for k in range(i+1, j):
                    bn_lst[k] = 0
                if j == length:
                    bn_lst.append(1)
                else:
                    bn_lst[j] = 1
                i = j
            elif j-i == 1:
                i = j
            else:
                i += 1
                j = i

    for i in range(1, len(bn_lst)):
        if bn_lst[i-1] == 1 and bn_lst[i]== -1:
            bn_lst[i-1] = -1
            bn_lst[i] = 0

    answers.append((len(bn_lst), bn_lst))

for length, lst in answers:
    print(length)
    print(" ".join(map(str, lst)))
