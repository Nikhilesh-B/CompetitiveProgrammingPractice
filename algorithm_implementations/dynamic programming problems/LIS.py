import bisect

t = int(input())
answers = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    backtrack = [-1 for _ in range(n)]
    dlis = []
    list_of_idxs = []
    last_idx = -1

    for i, num in enumerate(a):
        j = bisect.bisect_left(dlis, num)
        if j == len(dlis):
            if j == 0:
                backtrack[i] = -1
            else:
                backtrack[i] = list_of_idxs[j-1]

            list_of_idxs.append(i)
            dlis.append(num)
            last_idx = i
        elif dlis[j] > num:
            dlis[j] = num
            list_of_idxs[j] = i
            if j == 0:
                backtrack[i] = -1
            else:
                backtrack[i] = list_of_idxs[j-1]

            last_idx = i

    final_list = []

    while last_idx != -1:
        final_list.append(a[last_idx])
        last_idx = backtrack[last_idx]

    final_list.reverse()
    answers.append(final_list)

for ans in answers:
    print(" ".join(map(str, ans)))
