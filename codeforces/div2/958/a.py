t = int(input())
answers = []


def solve(n, k, saved_sums):
    if (n, k) in saved_sums:
        return saved_sums[(n, k)]
    elif n == 1:
        saved_sums[(n, k)] = 0
        return 0
    elif n <= k:
        saved_sums[(n, k)] = 1
        return 1
    else:
        saved_sums[(n, k)] = solve(n-k+1, k, saved_sums)+1
        return saved_sums[(n, k)]


for _ in range(t):
    n_k = list(map(int, input().split()))
    n = n_k[0]
    k = n_k[1]
    saved_sums = {}
    answers.append(solve(n, k, saved_sums))


for answer in answers:
    print(answer)
