t = int(input())
answers = []


def solve(n, m, k, a):
    goal = n

    queue = [(-1, 0)]
    explored = set()

    while queue:
        current = queue.pop(0)
        c_pos = current[0]
        c_swim = current[1]
        if c_pos == goal:
            return "YES"
        if current not in explored:
            explored.add(current)

            if c_pos == -1 or a[c_pos] == "L":
                for j in range(1, m+1):
                    if c_pos+j == n and (c_pos+j, c_swim) not in explored:
                        queue.append((c_pos+j, c_swim))
                        break
                    elif a[c_pos+j] != 'C' and (c_pos+j, c_swim) not in explored:
                        queue.append((c_pos+j, c_swim))

            if c_swim < k:
                if c_pos+1 == n and (c_pos+1, c_swim+1) not in explored:
                    queue.append((c_pos+1, c_swim+1))
                elif a[c_pos+1] != 'C' and (c_pos+1, c_swim+1) not in explored:
                    queue.append((c_pos+1, c_swim+1))

    return "NO"


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
