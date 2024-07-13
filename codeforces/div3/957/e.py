import sys
sys.set_int_max_str_digits(1000000)


def delete_rhs_digits(len_n, str_n, a, b):
    new_num = str_n*((a*len_n-b)//len_n)

    return int(str[:-x])


def satisfy(n, a, b):
    str_n = str(n)
    len_n = len(str_n)
    if (len_n*a <= b):
        return False
    elif (delete_rhs_digits(len_n, str_n, a, b) == n*a-b):
        return True
    return False


t = int(input())

answers = []

for _ in range(t):
    n = int(input())

    ans = []
    for a in range(1, 10001):
        b = min(10000, n*a)
        if satisfy(a, b, n):
            ans.append((a, b))

    answers.append((len(ans), ans))


for length, lst in answers:
    print(length)
    for a, b in lst:
        print(a, b)
