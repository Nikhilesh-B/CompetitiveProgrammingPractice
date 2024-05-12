def all_same(s):
    return all(c == s[0] for c in s)


def rearrange(s):
    char_first = s[0]
    swp_idx = 0
    for i, c in enumerate(s):
        if c != char_first:
            swp_idx = i
            break
    return s[swp_idx]+s[1:swp_idx]+s[0]+s[swp_idx+1:]


if __name__ == "__main__":
    t = int(input())
    strings = []
    for _ in range(t):
        s = input()
        strings.append(s)

    for s in strings:
        if all_same(s):
            print("NO")
        else:
            print("YES")
            print(rearrange(s))
