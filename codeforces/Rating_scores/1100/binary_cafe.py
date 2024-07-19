from math import log, floor
t = int(input())

answers = []

for _ in range(t):
    n_k = list(map(int, input().split()))
    n = n_k[0]
    k = n_k[1]

    exponent = min(k, floor(log(n, 2)))
    print("exponent: ", exponent)
    answers.append(2**(exponent)+1)

for answer in answers:
    print(answer)
