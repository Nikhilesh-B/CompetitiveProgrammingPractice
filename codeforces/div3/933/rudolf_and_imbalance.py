import bisect


def process_case(n: int, m: int, k: int, a: list[int], d: list[int], f: list[int]):
    a.sort()
    d.sort()
    f.sort()
    target_value = 0
    max_difference = -1
    max_idx = -1
    for i in range(n-1):
        if max_difference < a[i+1]-a[i]:
            max_difference = a[i+1]-a[i]
            target_value = (a[i+1]-a[i])//2
            max_idx = i

    best_difference = max_difference

    for d_num in d:
        f_target = target_value-d_num
        closest_value_less_than = bisect.bisect_left(f, f_target)
        closest_value_greater_than = bisect.bisect_right(f, f_target)
        a_i = a[max_idx]
        a_i_1 = a[max_idx+1]
        v1 = a_i_1-closest_value_greater_than
        v2 = closest_value_greater_than-a_i
        v3 = a_i_1-closest_value_less_than
        v4 = closest_value_less_than-a_i
        if (a_i <= closest_value_greater_than <= a_i_1):
            best_difference = min(max(v1, v2), best_difference)
        if (a_i <= closest_value_less_than <= a_i_1):
            best_difference = min(max(v3, v4), best_difference)

    return best_difference


if __name__ == "__main__":
    t = int(input())
    answers = []

    for _ in range(t):
        n, m, k = map(int, input().split())
        a = list(map(int, input().split()))
        d = list(map(int, input().split()))
        f = list(map(int, input().split()))
        ans = process_case(n, m, k, a, d, f)
        answers.append(ans)

    for a in answers:
        print(a)
