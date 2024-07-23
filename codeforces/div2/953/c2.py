t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(range(1, n + 1))

    if k % 2 == 1:
        print("NO")
        continue

    max_possible_sum = (n // 2) * (n // 2 + 1)
    if k > max_possible_sum:
        print("NO")
        continue

    l, r = 0, n - 1
    while k > 0 and l < r:
        diff = r - l
        if k >= 2 * diff:
            a[l], a[r] = a[r], a[l]
            k -= 2 * diff
            l += 1
            r -= 1
        else:
            if k > 0 and k % 2 == 0:
                mid = l + k // 2
                a[l], a[mid] = a[mid], a[l]
                k = 0
            break

    print("YES")
    print(" ".join(map(str, a)))