t = int(input())
answers = []
for _ in range(t):
    x_y_k = list(map(int, input().split()))
    x = x_y_k[0]
    y = x_y_k[1]
    k = x_y_k[2]

    coords = []

    if k % 2 == 1:
        coords.append((x, y))
        k -= 1

    for i in range(1, k//2+1):
        coords.append((x+i, y))
        coords.append((x-i, y))

    answers.append(coords)

for ans in answers:
    for x, y in ans:
        print(x, y)
