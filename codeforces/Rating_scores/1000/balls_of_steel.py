t = int(input())

answers = []

for _ in range(t):
    n_k = list(map(int, input().split()))
    n = n_k[0]
    k = n_k[1]
    points = []

    for _ in range(n):
        x_y = list(map(int, input().split()))
        x = x_y[0]
        y = x_y[1]
        points.append((x, y))

    nextItr = False

    for i in range(n):
        x1, y1 = points[i]
        neighs = 0
        for j in range(n):
            x2, y2 = points[j]
            if abs(x1-x2) + abs(y1-y2) > k:
                break
            else:
                neighs += 1
        if neighs == n:
            answers.append(1)
            nextItr = True
            break

    if nextItr:
        continue
    else:
        answers.append(-1)

for answer in answers:
    print(answer)
