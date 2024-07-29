t = int(input())
answers = []


def transpose(c):
    newc = [[0 for _ in range(len(c))] for _ in range(len(c[0]))]

    for i in range(len(c)):
        for j in range(len(c[0])):
            newc[j][i] = c[i][j]

    return newc


def process(c):
    total = 0
    for row in c:
        row.sort()
        lsum = 0
        for i, num in enumerate(row):
            if i == 0:
                continue
            else:
                lsum += num-row[0]
        total += lsum

        for i, num in enumerate(row):
            if i == 0:
                continue
            else:
                lsum = lsum-(len(row)-i)*(num-row[i-1])
                total += lsum

    return total


for _ in range(t):
    n_m = list(map(int, input().split()))
    n = n_m[0]
    m = n_m[1]
    c = []
    for i in range(n):
        row = list(map(int, input().split()))
        c.append(row)

    c = transpose(c)
    answers.append(process(c))


for ans in answers:
    print(ans)
