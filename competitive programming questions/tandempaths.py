t = int(input())
for _ in range(t):
    case = input()
    n = len(case)
    dp = [[0 for _ in range(n)] for _ in range(n)]

    for diag in range (1,n,2):
        for i in range(0,n-diag):
            first_letter = case[i]
            last_letter = case[i+diag]
            if diag == 1:
                if first_letter==last_letter or first_letter=="?" or last_letter=="?":
                    dp[i][i+diag] = 2 
                else:
                    dp[i][i+diag] = 0 
            else: 
                if first_letter==last_letter or first_letter=="?" or last_letter=="?":
                    dp[i][i+diag] = dp[i-1][i+diag-1]+2
                else:
                    dp[i][i+diag] = dp[i-1][i+diag-1]

    print(dp[0][0-1])