s = input().strip()


def is_subsequence(sub, s):
    # Checks if `sub` is a subsequence of `s`
    j = 0
    for ch in s:
        if ch == sub[j]:
            j += 1
            if j == len(sub):
                return True
    return False


def reverse_subseq_indices(start, end, s):
    # Get the indices of the subsequence from start to end in `s` and reverse them
    i = start
    indices = []
    while i <= end:
        indices.append(i)
        i += 1
    return indices[::-1]


# If "columbia" is not a subsequence of s, no operations are needed
if not is_subsequence("columbia", s):
    print("NO")
    exit()

# Try reversing the first occurrence of "columbia"
i = 0
start = -1
end = -1
for ch in "columbia":
    i = s.find(ch, i)
    if start == -1:
        start = i
    end = i
    i += 1

indices = reverse_subseq_indices(start, end, s)
new_s = s[:start] + s[start:end+1][::-1] + s[end+1:]

# If "columbia" is not a subsequence of the new string, output the indices
if not is_subsequence("columbia", new_s):
    print(len(indices))
    print(" ".join(map(str, indices)))
else:
    print("NO")
