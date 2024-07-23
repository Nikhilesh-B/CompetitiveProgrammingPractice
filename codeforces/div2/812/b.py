from collections import deque

t = int(input())

answers = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ordered = list(set(a))
    ordered.sort()

    dq = deque(a)

    current_idx = 0
    falseFlag = False

    while dq and current_idx < len(ordered):
        min = ordered[current_idx]
        if dq[0] != min and dq[-1] != min:
            falseFlag = True
            break

        while dq and dq[0] == min:
            dq.popleft()

        while dq and dq[-1] == min:
            dq.pop()

        current_idx += 1

    if falseFlag or dq:
        answers.append("NO")
        continue

    else:
        answers.append("YES")

for ans in answers:
    print(ans)
