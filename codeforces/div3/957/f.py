t = int(input())

answers = []


for _ in range(t):
    n_x = input().split()
    n = int(n_x[0])
    x = int(n_x[1])
    a = list(map(int, input().split()))

    factors_of_x = set()

    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            factors_of_x.add(i)
            factors_of_x.add(x // i)
    
    factors_sofar = set()
    segments = 1

    for i in range(n):
        if a[i] in factors_of_x:
            factors_sofar.add(a[i])
            for factor in factors_of_x:
                if a[i] * factor < x:
                    factors_sofar.add(a[i]*factor)
                elif a[i] * factor == x:
                    segments += 1
                    factors_sofar = set()
                    break
    
    answers.append(segments)

for ans in answers:
    print(ans)