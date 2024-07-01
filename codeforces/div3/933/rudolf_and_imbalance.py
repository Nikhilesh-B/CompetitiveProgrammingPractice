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
            target_value = (a[i+1]-a[i])//2+a[i]
            max_idx = i

    differences.sort()

    for d_num in d:
        f_target = target_value-d_num
        a_i = a[max_idx]
        a_i_1 = a[max_idx+1]
        b1 = 0 <= bisect.bisect_left(f, f_target) <= k-1
        b2 = 0 <= bisect.bisect_right(f, f_target) <= k-1

        if (b1 and b2):
            closest_value_less_than = f[bisect.bisect_left(f, f_target)]
            closest_value_greater_than = f[bisect.bisect_right(f, f_target)]
            b11 = a_i <= closest_value_less_than <= a_i_1
            b22 = a_i <= closest_value_greater_than <= a_i_1

            if b11 and b22:
                v1 = a_i_1-closest_value_less_than
                v2 = closest_value_less_than-a_i
                v3 = a_i_1-closest_value_greater_than
                v4 = closest_value_greater_than-a_i
                minval1 = min(v1, v2)
                maxval1 = max(v1, v2)
                minval2 = min(v3, v4)
                maxval2 = max(v3, v4)

                if maxval2 > maxval1 and differences[-1] > maxval1:
                    differences[-1] = maxval1
                    differences.insert(0, minval1)

                elif maxval1 >= maxval2 and differences[-1] > maxval2:
                    differences[-1] = maxval2
                    differences.insert(0, minval2)

            elif b11:
                v1 = a_i_1-closest_value_less_than
                v2 = closest_value_less_than-a_i
                minval = min(v1, v2)
                maxval = max(v1, v2)
                if differences[-1] > maxval:
                    differences[-1] = maxval
                    differences.insert(0, minval)

            elif b22:
                v3 = a_i_1-closest_value_greater_than
                v4 = closest_value_greater_than-a_i
                minval = min(v3, v4)
                maxval = max(v3, v4)
                if differences[-1] > maxval:
                    differences[-1] = maxval
                    differences.insert(0, minval)

        elif (b1):
            closest_value_less_than = f[bisect.bisect_left(f, f_target)]
            if (a_i <= closest_value_less_than <= a_i_1):
                v1 = a_i_1-closest_value_less_than
                v2 = closest_value_less_than-a_i
                minval = min(v1, v2)
                maxval = max(v1, v2)
                if differences[-1] > maxval:
                    differences[-1] = maxval
                    differences.insert(0, minval)

        elif (b2):
            closest_value_greater_than = f[bisect.bisect_right(f, f_target)]
            if (a_i <= closest_value_greater_than <= a_i_1):
                v3 = a_i_1-closest_value_greater_than
                v4 = closest_value_greater_than-a_i
                minval = min(v3, v4)
                maxval = max(v3, v4)
                if differences[-1] > maxval:
                    differences[-1] = maxval
                    differences.insert(0, minval)

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
