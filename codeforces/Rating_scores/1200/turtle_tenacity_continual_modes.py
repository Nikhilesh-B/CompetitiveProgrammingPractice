t = int(input())
answers = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    min_val = min(a)
    min_count = a.count(min_val)

    if min_count > 1:
        flag = 0
        for num in a:
            if num % min_val:
                answers.append("YES")
                flag = 1
                break
        if not flag:
            answers.append("NO")
    else:
        answers.append("YES")

for ans in answers:
    print(ans)