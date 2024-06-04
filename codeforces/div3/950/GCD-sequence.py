
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def is_new_gcd_non_decreasing(gcd_a_new):
    for i in range(1, len(gcd_a_new)):
        if gcd_a_new[i] < gcd_a_new[i-1]:
            return False
    return True


def process_case(n, a):
    gcd_a = [0 for i in range(n-1)]

    for i in range(n-1):
        gcd_a[i] = gcd(a[i], a[i+1])

    decreases = 0
    idx_of_decrease = -2

    for i in range(1, n-1):
        if gcd_a[i] < gcd_a[i-1]:
            if i-1!=idx_of_decrease:
                decreases += 1
                idx_of_decrease = i

    if decreases > 1:
        print("NO")
        return

    if decreases == 0:
        print("YES")
        return

    else:
        cand1 = idx_of_decrease-1
        cand2 = idx_of_decrease
        cand3 = idx_of_decrease+1

        cands = [cand1, cand2, cand3]
        for cand in cands:
            if cand == 0:
                new_gcd = gcd_a[1:]
                if is_new_gcd_non_decreasing(new_gcd):
                    print("YES")
                    return
            elif cand == n-1:
                new_gcd = gcd_a[:-1]
                if is_new_gcd_non_decreasing(new_gcd):
                    print("YES")
                    return
            elif cand == 1:
                high_bound = gcd_a[cand+1]
                mid = gcd(a[cand-1], a[cand+1])
                if mid <= high_bound:
                    print("YES")
                    return
            elif cand == n-2:
                low_bound = gcd_a[cand-2]
                mid = gcd(a[cand-1], a[cand+1])
                if low_bound <= mid:
                    print("YES")
                    return
            else:
                low_bound = gcd_a[cand-2]
                high_bound = gcd_a[cand+1]
                mid = gcd(a[cand-1], a[cand+1])
                if low_bound <= mid and mid <= high_bound:
                    print("YES")
                    return
        print("NO")
        return


if __name__ == "__main__":
    t = int(input())
    n_s = {}
    a_s = {}

    for i in range(t):
        n_s[i] = int(input())
        a_s[i] = list(map(int, input().split()))

    for i in range(t):
        n = n_s[i]
        a = a_s[i]
        process_case(n, a)  