import math
t = int(input())
ans = []

for _ in range(t):
    k = int(input())
    an = k
    squares_below = math.floor(math.sqrt(k))
    
    cand = k+1
    while squares_below>0:
        if cand!=math.floor(math.sqrt(cand))**2:
            squares_below-=1
        cand+=1
        an+=1
    ans.append(an)

for an in ans:
    print(an)