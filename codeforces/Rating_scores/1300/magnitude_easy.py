t = int(input())

answers = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    c = 0

    # postfix sum
    postfix_sum = [0] * n
    postfix_sum[-1] = a[-1]
    for i in range(n-2, -1, -1):
        postfix_sum[i] = postfix_sum[i+1] + a[i]

    # now the sume:

    for i in range(n-1):
        if a[i] > 0:
            c += a[i]
        else:
            pass        


for ans in answers:
    print(ans)
