from collections import deque
import math

# Read inputs
N, D = map(int, input().split())
p = list(map(int, input().split()))

# Sort the list in descending order
p.sort(reverse=True)
p = deque(p)
w = 0

while p:
    cpower = p.popleft()
    if cpower > D:
        w += 1
    else:
        needed = math.ceil((D + 1) / cpower) - 1
        if len(p) >= needed:
            for _ in range(needed):
                p.pop()
            w += 1
        else:
            break

print(w)
