import bisect


def process_case(n: int, m: int, k: int, a: list[int], d: list[int], f: list[int]):
    a.sort()
    d.sort()
    f.sort()
    target_value = 0
    max_difference = -1
    max_idx = -1
    differences = []
    for i in range(n-1):
        differences.append(a[i+1]-a[i])
        if max_difference < a[i+1]-a[i]:
            max_difference = a[i+1]-a[i]
            target_value = (a[i+1]-a[i])//2 + a[i]
            max_idx = i

    differences.sort()

    print(differences)
    for d_num in d:
        f_target = target_value - d_num
        a_i = a[max_idx]-d_num
        a_i_1 = a[max_idx+1]-d_num
        print(a_i, a_i_1)

        left_idx = bisect.bisect_left(f, f_target)
        if left_idx < k:
            closest_value_less_than = f[left_idx -
                                        1] if left_idx > 0 and f[left_idx] != f_target else left_idx
            if a_i <= closest_value_less_than <= a_i_1:
                v1 = a_i_1 - closest_value_less_than
                v2 = closest_value_less_than - a_i
                differences[-1] = min(max(v1, v2), differences[-1])

        right_idx = bisect.bisect_right(f, f_target)
        if right_idx < k:
            closest_value_greater_than = f[right_idx] if right_idx < len(
                f) else float('inf')
            if a_i <= closest_value_greater_than <= a_i_1:
                v3 = a_i_1 - closest_value_greater_than
                v4 = closest_value_greater_than - a_i
                differences[-1] = min(max(v3, v4), differences[-1])
    print(differences)
    differences.sort()
    return differences[-1]


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
