t = int(input())
answers = []

for _ in range(t):
    n_k = list(map(int, input().split()))
    n = n_k[0]
    k = n_k[1]
    s = input()
    s = [c for c in s]
    counts = {}

    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    odd_counts = 0

    for value in counts.values():
        if value % 2 == 1:
            odd_counts += 1

    if (n-k) % 2 == 0:
        if odd_counts > k:
            answers.append("NO")
        else:
            answers.append("YES")

    else:
        if odd_counts-1 > k:
            answers.append("NO")
        else:
            answers.append("YES")

for answer in answers:
    print(answer)
