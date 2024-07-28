import math
from collections import OrderedDict

# t = int(input())

# calculateing all_primes less than 2*10^5
m = 2*(10**5)+1

non_primes = set()
primes = set()

for j in range(1, math.floor(math.sqrt(m))+1):
    if j not in non_primes:
        p = 2
        while p*j <= m:
            non_primes.add(p*j)
            p += 1

for j in range(2, m+1):
    if j not in non_primes:
        primes.add(j)

print(1 in primes)

ncolors = [1]
colors = [1]

coloring = {1: [1]}

for nx in range(2, m+1):
    continueFlag = False
    for color in sorted(coloring.keys(), reverse=True):
        node_set = coloring[color]
        fail = False
        for node in node_set:
            if nx ^ node in primes:
                fail = True
                break

        if fail:
            coloring[color].append(nx)
            ncolors.append(ncolors[-1])
            colors.append(color)
            continueFlag = True

        if continueFlag:
            break

    if not fail:
        num_c = ncolors[-1]
        coloring[num_c+1] = [nx]
        ncolors.append(num_c+1)
        colors.append(num_c+1)

# for _ in range(t):
#     n = int(input())
