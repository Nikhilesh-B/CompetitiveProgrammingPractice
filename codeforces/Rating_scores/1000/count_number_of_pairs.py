t = int(input())
answers = []

for _ in range(t):
    n_k = list(map(int, input().split()))
    n = n_k[0]
    k = n_k[1]
    s = input()

    burls = 0

    chars = set()
    upper_chars = dict()
    lower_chars = dict()

    for i in range(n):
        c = s[i]
        chars.add(c.upper())

        if c.isupper():
            if c not in upper_chars:
                upper_chars[c] = 0
            upper_chars[c] += 1

        if c.islower():
            if c.upper() not in lower_chars:
                lower_chars[c.upper()] = 0
            lower_chars[c.upper()] += 1

    differences = []

    for c in chars:
        if c in upper_chars and c in lower_chars:
            burls += min(upper_chars[c], lower_chars[c])
            differences.append(abs(upper_chars[c] - lower_chars[c]))
        elif c in upper_chars:
            differences.append(upper_chars[c])
        elif c in lower_chars:
            differences.append(lower_chars[c])

    # print("Burls first", burls)
    # print("upper chars", upper_chars)
    # print("lower chars", lower_chars)

    differences.sort()
    # print("Differences", differences)
    n_differences = list(filter(lambda x: x >= 2, differences))
    n_differences = list(map(lambda x: x//2, n_differences))

    # print("N differences", n_differences)

    rcount = 0
    for dif in n_differences:
        if rcount + dif >= k:
            rcount = k
            break
        rcount += dif

    answers.append(burls + rcount)


for answer in answers:
    print(answer)
