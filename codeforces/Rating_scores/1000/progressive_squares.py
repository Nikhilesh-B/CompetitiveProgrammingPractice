t = int(input())
answers = []

for _ in range(t):
    n_c_d = list(map(int, input().split()))
    n = n_c_d[0]
    c = n_c_d[1]
    d = n_c_d[2]
    a = list(map(int, input().split()))

    mina = min(a)
    number_set = {mina: 1}

    for i in range(n):
        for j in range(1, n):
            if (mina+j*d) in number_set:
                number_set[mina+j*d] += 1
            else:
                number_set[mina+j*d] = 1
        if i != n-1:
            mina = mina+c
            if mina in number_set:
                number_set[mina] += 1
            else:
                number_set[mina] = 1


    fail = False

    for num in a:
        if num in number_set:
            if number_set[num] > 1:
                number_set[num] -= 1
            else:
                number_set.pop(num)
        else:
            fail = True
            break

    if fail:
        answers.append('NO')

    elif len(number_set) == 0:
        answers.append('YES')

    else:
        answers.append('NO')

for ans in answers:
    print(ans)
