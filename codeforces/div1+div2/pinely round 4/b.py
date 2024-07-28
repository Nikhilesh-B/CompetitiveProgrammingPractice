t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))
    a = [0 for _ in range(n)]

    fail = False

    a[0] = b[0]
    a[1] = b[0]

    for i in range(1, n-1):
        target = b[i]
        prev_saved_num = a[i]

        b1 = bin(prev_saved_num)[2:]
        len_b1 = len(b1)
        b1 = "0"*(31-len_b1)+b1

        b2 = bin(target)[2:]
        len_b2 = len(b2)
        b2 = "0"*(31-len_b2)+b2
        b1 = [c for c in b1]
        b2 = [c for c in b2]
        for j in range(31):
            if b1[j] == '0' and b2[j] == '0':
                continue
            elif b1[j] == '1' and b2[j] == '0':
                continue
            elif b1[j] == '0' and b2[j] == '1':
                b1[j] = '1'
            else:
                continue

        a[i] = int("0b"+"".join(b1), 2)
        a[i+1] = target

    for i in range(n-1):
        if a[i] & a[i+1] != b[i]:
            fail = True
            break

    if fail:
        print(-1)
        continue
    else:
        print(" ".join(map(str, a)))
