
def remove_any_repeats(c_list):
    seen = set()
    new_list = []
    duplicates = 0

    for c in c_list:
        if (c not in seen):
            new_list.append(c)
            seen.add(c)
        else:
            duplicates += 1

    return new_list, duplicates


def process_case(n, m, s_str, ind, c_str):
    ind.sort()
    c = [char for char in c_str]
    s = [char for char in s_str]
    c.sort()

    ind, duplicates = remove_any_repeats(ind)
    if (duplicates != 0):
        c = c[:-duplicates]

    zipped_list = list(zip(ind, c))
    for i in range(len(zipped_list)):
        s[ind[i]-1] = zipped_list[i][1]

    print_list(s)


def print_list(s):
    dummy_string = ''
    for char in s:
        dummy_string += char
    print(dummy_string)


if __name__ == "__main__":
    t = int(input())
    n = {}
    m = {}
    s = {}
    ind = {}
    c = {}

    for i in range(t):
        n[i], m[i] = list(map(int, input().split()))
        s[i] = input()
        ind[i] = list(map(int, input().split()))
        c[i] = input()

    for i in range(t):
        process_case(n[i], m[i], s[i], ind[i], c[i])
