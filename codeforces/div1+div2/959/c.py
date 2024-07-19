import bisect

t = int(input())

answers = []

for _ in range(t):
    n_x = list(map(int, input().split()))
    n = n_x[0]
    x = n_x[1]

    a = list(map(int, input().split()))

    total_segments = 0

    # Compute prefix sums
    prefix_sum = [0]
    for i in range(n):
        prefix_sum.append(prefix_sum[-1] + a[i])

    # Search for segments with inclusive sum <= x
    for i in range(n):
        search_num = prefix_sum[i] + x
        index = bisect.bisect_left(prefix_sum, search_num)
        # print("INDEX", i)
        # print("FOUND IDX", index)
        # print("SEARCH NUM", search_num)
        # print("PREFIX SUM current", prefix_sum[i])
        # print("PREFIX SUM:", prefix_sum)
        if index == len(prefix_sum):
            total_segments += (index - i)
        elif prefix_sum[index] > search_num:
            total_segments += (index - 1 - i)
        else:
            total_segments += (index - i)

    answers.append(total_segments)

for answer in answers:
    print(answer)