def column_sums(a, n, m):
    sums = []
    for i in range(m):
        s = 0
        for j in range(n):
            s += a[j][i]
        sums.append(s % 3)
    return sums


def row_sums(a, n, m):
    sums = []
    for i in range(n):
        sums.append(sum(a[i]) % 3)
    return sums


def process(a, b, n, m):
    a_row_sums = row_sums(a, n, m)
    a_column_sums = column_sums(a, n, m)
    b_row_sums = row_sums(b, n, m)
    b_column_sums = column_sums(b, n, m)

    if a_row_sums == b_row_sums and a_column_sums == b_column_sums:
        return "YES"
    else:
        return "NO"


t = int(input())
answers = []
for _ in range(t):
    n_m = list(map(int, input().split()))
    n = n_m[0]
    m = n_m[1]
    a = [[0 for _ in range(m)] for _ in range(n)]
    b = [[0 for _ in range(m)] for _ in range(n)]
    # taking in char by chat and converting to int
    for i in range(n):
        row = input()
        for j in range(m):
            a[i][j] = int(row[j])
    for i in range(n):
        row = input()
        for j in range(m):
            b[i][j] = int(row[j])

    answers.append(process(a, b, n, m))

for answer in answers:
    print(answer)
