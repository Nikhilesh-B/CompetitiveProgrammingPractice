t = int(input())
answers = []


def solve(n, m, k, a):
    current_swim = 0
    i = -1

    while i < n:
        if current_swim > k:
            return "NO"

        if i == -1 or a[i] == "L":
            jumped = False
            for j in range(m, 0, -1):
                if i + j == n or (i + j < n and a[i + j] == "L"):
                    i += j
                    jumped = True
                    break

            if not jumped:
                for j in range(m, 0, -1):
                    if i + j < n and a[i + j] != 'C':
                        i += j
                        jumped = True
                        break
            if jumped:
                continue

        if a[i] == 'C':
            return "NO"

        else:
            current_swim += 1
            i += 1

    if current_swim > k:
        return "NO"

    return "YES"


for _ in range(t):
    n_m_k = list(map(int, input().split()))
    n = n_m_k[0]
    m = n_m_k[1]
    k = n_m_k[2]

    a_str = input()
    a = [c for c in a_str]

    answers.append(solve(n, m, k, a))

for answer in answers:
    print(answer)
