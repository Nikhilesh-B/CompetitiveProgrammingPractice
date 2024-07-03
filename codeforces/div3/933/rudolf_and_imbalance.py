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

    insert_val_mn = None
    insert_val_mx = None

    for d_num in d:
        f_target = target_value-d_num
        lo = a[max_idx]-d_num
        hi = a[max_idx+1]-d_num
        lidx = bisect.bisect_left(f, f_target)
        ridx = bisect.bisect_right(f, f_target)
        lval, rval = None, None
        linrange, rinrange = False, False
        if 0 <= lidx <= k:
            if lidx != k and f[lidx] == f_target:
                lval = f[lidx]
            else:
                lval = f[lidx-1]
            if lo <= lval <= hi:
                linrange = True
        if 0 <= ridx < k:
            rval = f[ridx]
            if lo <= rval <= hi:
                rinrange = True

        if (lval != None and linrange):
            vl1, vl2 = lval-lo, hi-lval
            if max(vl1, vl2) < max_difference:
                insert_val_mx = max(vl1, vl2)
                insert_val_mn = min(vl1, vl2)
                max_difference = insert_val_mx

        if (rval != None and rinrange):
            vr1, vr2 = rval-lo, hi-rval
            if max(vr1, vr2) < max_difference:
                insert_val_mx = max(vr1, vr2)
                insert_val_mn = min(vr1, vr2)
                max_difference = insert_val_mx

    if (insert_val_mx != None and insert_val_mn != None):
        differences.pop()
        # differences.append(insert_val_mn)
        differences.append(insert_val_mx)

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
