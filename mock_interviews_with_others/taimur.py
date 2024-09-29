def main(a, b):
    m, n = len(a), len(b)
    dp = [[0 for j in range(n + 1)] for i in range(m + 1)]

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            # Recurrence Relation
            # If a[i] != b[j]: max of the previous solutions
            # Else: just add 1 to the max
            dp[i][j] = max(dp[i][j + 1], dp[i + 1][j], dp[i + 1][j + 1]) + (1 if a[i] == b[j] else 0)
    
    for row in dp:
        print(" ".join(map(str, row)))

    s = dp[0][0]

    return len(a) + len(b) - 2 * s

a = "cxxxusssjrrssky"
b = "ttttcurrywwww"

res = main(a, b)
print(res)