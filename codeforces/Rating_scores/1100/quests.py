t = int(input())

answers = []

for _ in range(t):
    n_k = list(map(int, input().split()))
    n = n_k[0]
    k = n_k[1]
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    for i in range(1, n):
        b[i] = max(b[i], b[i-1])

    mx = 0
    existing_calc = 0
    for i in range(1, min(k, n)+1):
        existing_calc += a[i-1]
        repeats = b[i-1]*(k-i)
        mx = max(mx, existing_calc+repeats)

    print(mx)
