def dot_product(a, b):
    assert (len(a) == len(b))
    sm = 0
    for i, num in enumerate(a):
        a[i] *= b[i]
        sm += a[i]
    return sm


def num_to_feed(strs, n_stew):
    left_pass = [0 for _ in range(n_stew)]
    right_pass = [0 for _ in range(n_stew)]
    strs.sort()

    mn = strs[0]
    mx = strs[-1]
    for i, stren in enumerate(strs):
        if stren != mn:
            left_pass[i] = 1

    for i in range(n_stew-1, -1, -1):
        if strs[i] != mx:
            right_pass[i] = 1

    return dot_product(left_pass, right_pass)


if __name__ == "__main__":
    n_stew = int(input())
    strs = input().split(" ")
    strs = [int(s) for s in strs]
    print(num_to_feed(strs, n_stew))
