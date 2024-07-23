t = int(input())
answers = []
for _ in range(t):
    n_m = list(map(int, input().split()))
    n = n_m[0]
    m = n_m[1]
    if m > n:
        answers.append("NO")
    elif m == n:
        answers.append("YES")
    else:
        if (n-m) % 2 == 0:
            answers.append("YES")
        else:
            answers.append("NO")

for answer in answers:
    print(answer)
