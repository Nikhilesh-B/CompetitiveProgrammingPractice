import math


def compute_prefix_sum(arr, n):
    prefix_sum = [0] * n
    prefix_sum[0] = arr[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i-1] + arr[i]
    return prefix_sum


def compute_suffix_sum(arr, n):
    suffix_sum = [0] * n
    suffix_sum[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        suffix_sum[i] = suffix_sum[i+1] + arr[i]
    return suffix_sum

# here we print the cases as they are needed.


def print_case(f, s, t, i, j, n):
    i += 1
    j += 1
    if f == "a" and s == "b" and t == "c":
        print(1, i, i+1, j, j+1, n)
    elif f == "a" and s == "c" and t == "b":
        print(1, i, j+1, n, i+1, j)
    elif f == "b" and s == "a" and t == "c":
        print(i+1, j, 1, i,  j+1, n)
    elif f == "b" and s == "c" and t == "a":
        print(j+1, n, 1, i, i+1, j)
    elif f == "c" and s == "a" and t == "b":
        print(i+1, j, j+1, n,  1, i)
    elif f == "c" and s == "b" and t == "a":
        print(j+1, n, i+1, j,  1, i)


def possible(f, s, t, n, psums, ssums, total):
    psum1 = psums[f]
    ssum1 = ssums[f]
    psum2 = psums[s]
    ssum2 = ssums[s]
    psum3 = psums[t]
    ssum3 = ssums[t]

    target = math.ceil(total / 3)

    for i in range(n):
        if psum1[i] >= target:
            for j in range(i+1, n-1):
                if (total - psum2[i] - ssum2[j+1]) >= target and ssum3[j+1] >= target:
                    print_case(f, s, t, i, j, n)
                    return True
                if j == n-2:
                    return False

    return False


def solve(a, b, c, n):
    total = sum(a)
    apsum = compute_prefix_sum(a, n)
    bpsum = compute_prefix_sum(b, n)
    cpsum = compute_prefix_sum(c, n)

    assum = compute_suffix_sum(a, n)
    bssum = compute_suffix_sum(b, n)
    cssum = compute_suffix_sum(c, n)

    psums = {'a': apsum, 'b': bpsum, 'c': cpsum}
    ssums = {'a': assum, 'b': bssum, 'c': cssum}

    pos1 = possible("a", "b", "c", n, psums, ssums, total)
    if pos1:
        return
    pos2 = possible("a", "c", "b", n, psums, ssums, total)
    if pos2:
        return
    pos3 = possible("b", "a", "c", n, psums, ssums, total)
    if pos3:
        return
    pos4 = possible("b", "c", "a", n, psums, ssums, total)
    if pos4:
        return
    pos5 = possible("c", "a", "b", n, psums, ssums, total)
    if pos5:
        return
    pos6 = possible("c", "b", "a", n, psums, ssums, total)
    if pos6:
        return

    print("-1")
    return


t = int(input())
answers = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    solve(a, b, c, n)
