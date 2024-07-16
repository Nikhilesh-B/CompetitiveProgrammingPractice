t = int(input())

answers = []

for _ in range(t):
    n_k = list(map(int, input().split()))
    n = n_k[0]
    k = n_k[1]
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))

    ht = {}

    for i, pos in enumerate(x):
        if abs(pos) in ht:
            ht[abs(pos)] += a[i]
        else:
            ht[abs(pos)] = a[i]

    mx_pos = max(ht.keys())

    ammo_value = 0

    fail = False
    for i in range(1, mx_pos+1):
        ammo_value += k
        if i in ht:
            ammo_value -= ht[i]

        if ammo_value < 0:
            fail = True
            break

    if fail:
        answers.append('NO')
    else:
        answers.append('YES')

for ans in answers:
    print(ans)
