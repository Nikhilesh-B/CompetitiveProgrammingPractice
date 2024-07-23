t = int(input())
answers = []

for _ in range(t):
    n_m = list(map(int, input().split()))
    n = n_m[0]
    m = n_m[1]
    if m == 0:
        answers.append(n)
        continue

    upper = n+m
    lower = max(n-m, 0)

    bn = bin(n)[2:]
    bu = bin(upper)[2:]
    bl = bin(lower)[2:]

    ln = len(bn)
    lu = len(bu)
    ll = len(bl)

    bl = "0"*(lu-ll)+bl
    bn = "0"*(lu-ln)+bn

    rbin = bn

    if lu > ln:
        rbin = "1"*lu

    elif ln > ll:
        rbin = "1"*ln

    else:
        if bu[0] == "1":
            rbin = "1"+rbin[1:]

        sbin = ""
        tbin = ""
        first1 = -1
        for i in range(1, ln):
            if bn[i] == "1" and first1 == -1 and bl[i] != bn[i]:
                first1 = i
                break
        if first1 != -1:
            sbin = bn[:first1]+"1"*(ln-first1)

        # print("sbin here", sbin)

        f1 = -1
        for i in range(1, ln):
            if bu[i] == "1" and f1 == -1 and bu[i] != bn[i]:
                f1 = i
                break
        if f1 != -1:
            tbin = bu[:f1]+"1"*(ln-f1)

        if sbin and tbin:
            rbin = ""
            for i in range(ln):
                if sbin[i] == "1" or tbin[i] == "1":
                    rbin += "1"
                else:
                    rbin += "0"
        elif sbin:
            rbin = sbin
        elif tbin:
            rbin = tbin

        # print("rbin here", rbin)
    answers.append(int(rbin, 2))

    # print("bl", bl)
    # print("bn", bn)
    # print("bu", bu)
    # print("rb", rbin)


for answer in answers:
    print(answer)
