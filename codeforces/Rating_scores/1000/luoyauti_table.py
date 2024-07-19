t = int(input())

answers = []

for _ in range(t):
    n_m = list(map(int, input().split()))
    n = n_m[0]
    m = n_m[1]
    b = list(map(int, input().split()))
    b.sort()
    total1 = 0
    total1 += (min(n, m)-1)*(b[-1]-b[1])
    total1 += (n*m-(min(n, m)-1)-1)*(b[-1]-b[0])

    total2 = 0
    total2 += (min(n, m)-1)*(b[-2]-b[0])
    total2 += (n*m-(min(n, m)-1)-1)*(b[-1]-b[0])

    answers.append(max(total1, total2))


for answer in answers:
    print(answer)
