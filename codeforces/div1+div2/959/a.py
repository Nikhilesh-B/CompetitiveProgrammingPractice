t = int(input())
answers = []
for _ in range(t):
    n_m = list(map(int, input().split()))
    n = n_m[0]
    m = n_m[1]

    a = []
    for i in range(n):
        lst = [int(x) for x in input().split()]
        lst = [x+1 if x != n*m else 1 for x in lst]
        a.append(lst)

    if n == 1 and m == 1:
        answers.append((-1, []))
        continue

    answers.append((1, a))

for answer in answers:
    if answer[0] == -1:
        print(-1)
    else:
        for row in answer[1]:
            print(' '.join(map(str, row)))
