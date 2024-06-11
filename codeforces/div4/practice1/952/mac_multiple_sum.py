def multiple_sum(x, n):
    vals = []
    k = 1
    while k*x <= n:
        vals.append(k*x)
        k += 1
    return sum(vals)


def process_case(n):
    max_val = -1
    max_answer = -1
    for j in range(2, n+1):
        val = multiple_sum(j, n)
        if val > max_val:
            max_val = val
            max_answer = j
    print(max_answer)


if __name__ == "__main__":
    t = int(input())
    n_s = []

    for _ in range(t):
        n = int(input())
        n_s.append(n)

    for i in range(t):
        n = n_s[i]
        process_case(n)
