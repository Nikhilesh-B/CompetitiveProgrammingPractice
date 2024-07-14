t = int(input())

answers = []


for _ in range(t):
    n_x = input().split()
    n = int(n_x[0])
    x = int(n_x[1])
    a = list(map(int, input().split()))

    factors_of_x = set()

    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            factors_of_x.add(i)
            factors_of_x.add(x // i)

    factors_sofar = set()
    segments = 1

    continue_flag = False
    for i in range(n):
        if a[i] in factors_of_x:
            add_factors = []
            for factor in factors_sofar:
                if a[i] * factor < x:
                    add_factors.append(a[i]*factor)
                elif a[i] * factor == x:
                    segments += 1
                    factors_sofar = set()
                    continue_flag = True
                    break
            if not continue_flag:
                for factor in add_factors:
                    factors_sofar.add(factor)
            else:
                continue_flag = False
            factors_sofar.add(a[i])

    answers.append(segments)

for ans in answers:
    print(ans)