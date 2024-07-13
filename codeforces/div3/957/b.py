t = int(input())
answers = []

for _ in range(t):
    n_k = list(map(int, input().split()))
    n = n_k[0]
    k = n_k[1]
    a = list(map(int, input().split()))
    a.sort()

    moves = 0
    for i in range(k-1):
        if a[i] >=2:
            moves += a[i] - 1
        moves+=a[i]
    
    answers.append(moves)

for answer in answers:
    print(answer)