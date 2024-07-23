t = int(input())

answers = []

for _ in range(t):
    n_a_b = list(map(int, input().split()))
    n = n_a_b[0]
    a = n_a_b[1]
    b = n_a_b[2]

    if a >= b:
        answers.append(n*a)
    else:
        k = min(n, b-a)
        if k == b-a:
            val = (n-k)*a + (k*(b+a+1))//2
        else:
            val = (k*(b+b-k+1))//2

        answers.append(int(val))

for answer in answers:
    print(answer)
