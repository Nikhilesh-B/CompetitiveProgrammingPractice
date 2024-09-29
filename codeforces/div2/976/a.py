import math

t = int(input())
ans = []

for _ in range(t):
    n_k = list(map(int, input().split()))
    n = n_k[0]
    k = n_k[1]

    an = 0

    if k == 1:
        ans.append(n)
        continue

    while n>=k:
        an+=1
        exp = math.floor(math.log(n,k))
        n -= k**exp
        
    an+=n
    ans.append(an)

for an in ans:
    print(an)