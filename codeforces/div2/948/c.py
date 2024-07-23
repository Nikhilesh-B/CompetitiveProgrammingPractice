t = int(input())
answers = []


def compute_GCD(a, b):
    if b == 0:
        return a
    else:
        return compute_GCD(b, a % b)


def compute_LCM_arr(a):
    b = a[0]
    if len(a) == 1:
        return b

    for i in range(1, len(a)):
        b = (b*a[i])/compute_GCD(b, a[i])
    return b


for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a_set = set(a)

    prod = 1
    for num in a:
        prod *= num

    LCM = int(compute_LCM_arr(a))

    print("LCM", LCM)

    while a and LCM in a_set:
        lval = a[-1]
        dprod = 1
        while a and a[-1] == lval:
            dprod *= a.pop()
        if not a:
            break
        prod /= dprod
        LCM = int(compute_LCM_arr(a))
        print("LCM", LCM)
        print(a)

    print(a)
    answers.append(len(a))

for ans in answers:
    print(ans)
