t = int(input())
answers = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    max_odd = -1

    for i in range(0, n, 2):
        max_odd = max(max_odd, a[i])

    answers.append(max_odd)

for ans in answers:
    print(ans)
