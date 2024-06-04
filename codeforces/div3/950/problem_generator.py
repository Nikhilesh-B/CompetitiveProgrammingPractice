if __name__ == "__main__":
    t = int(input())
    n_s = {}
    m_s = {}
    problems = {}

    for i in range(t):
        n, m = map(int, input().split())
        n_s[i] = n
        m_s[i] = m
        problem = str(input())
        problems[i] = problem

    

    for i in range(t):
        n = n_s[i]
        m = m_s[i]
        problem = problems[i]

        counts = {key:0 for key in ['A', 'B', 'C', 'D', 'E', 'F', 'G']}

        for char in problem:
            counts[char] += 1

        total = 0 
        for key in counts:
            if m > counts[key]:
                total += (m - counts[key])

        print(total)