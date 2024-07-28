import statistics
import math

t = int(input())


for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    k_choices = []
    k = 0
    passed = False

    for i in range(41):
        if sum(a) == 0:
            passed = True
            break

        avg = math.ceil(statistics.mean(a))
        k_choices.append(avg)
        a = [abs(num-avg) for num in a]
        k += 1

    if not passed:
        print(-1)
        continue
    print(k)
    print(" ".join(map(str, k_choices)))
