t = int(input())
answers = []
for _ in range(t):
    n = int(input())
    ords = []
    for _ in range(n):
        x_y = tuple(map(int, input().split()))
        ords.append(x_y)

    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0

    for x_y in ords:
        x = x_y[0]
        y = x_y[1]
        min_x = min(x, min_x)
        min_y = min(y, min_y)
        max_x = max(x, max_x)
        max_y = max(y, max_y)

    rval = 2*abs(min_x)+2*abs(min_y)+2*max_x+2*max_y

    answers.append(rval)

for ans in answers:
    print(ans)
