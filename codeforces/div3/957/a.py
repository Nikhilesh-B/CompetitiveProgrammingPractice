from itertools import permutations


t = int(input())
answers = []

for _ in range(t):
    a_b_c = list(map(int, input().split()))
    a = a_b_c[0]
    b = a_b_c[1]
    c = a_b_c[2]
    mx = a*b*c

    perms1 = list(permutations([5, 0, 0]))
    perms2 = list(permutations([3, 1, 1]))
    perms3 = list(permutations([4, 1, 0]))
    perms4 = list(permutations([2, 2, 1]))
    perms5 = list(permutations([3, 2, 0]))

    for perm in perms1:
        a1 = perm[0]
        b1 = perm[1]
        c1 = perm[2]
        mx = max(mx, (a+a1)*(b+b1)*(c+c1))

    for perm in perms2:
        a1 = perm[0]
        b1 = perm[1]
        c1 = perm[2]
        mx = max(mx, (a+a1)*(b+b1)*(c+c1))

    for perm in perms3:
        a1 = perm[0]
        b1 = perm[1]
        c1 = perm[2]
        mx = max(mx, (a+a1)*(b+b1)*(c+c1))

    for perm in perms4:
        a1 = perm[0]
        b1 = perm[1]
        c1 = perm[2]
        mx = max(mx, (a+a1)*(b+b1)*(c+c1))

    for perm in perms5:
        a1 = perm[0]
        b1 = perm[1]
        c1 = perm[2]
        mx = max(mx, (a+a1)*(b+b1)*(c+c1))

    answers.append(mx)

for answer in answers:
    print(answer)
