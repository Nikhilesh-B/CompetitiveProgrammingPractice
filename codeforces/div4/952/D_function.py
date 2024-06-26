def good_digits(k):
    good_count = 0
    for digit in range(0, 10):
        if digit*k < 10:
            good_count += 1
    return good_count


def process_case(l, r, k):
    total = 0
    good_count = good_digits(k)
    for i, num_digits in enumerate(range(l+1, r+1)):
        if i == 0:
            cases = (good_count-1)*good_count**(num_digits-1)
        else:
            cases *= good_count
        total += cases
    print(total % (10**9 + 7))

if __name__ == "__main__":
    t = int(input())
    l_r_k = []

    for _ in range(t):
        l_r_k.append(list(map(int, input().split())))

    for i in range(t):
        l, r, k = l_r_k[i]
        process_case(l, r, k)
