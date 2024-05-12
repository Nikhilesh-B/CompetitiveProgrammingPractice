if __name__ ==  "__main__":
    t = int(input())
    strings = []
    for _ in range(t):
        s = list(map(int, input().split()))
        strings.append(s)
    for case in strings: 
        alice_strings = case[:2]
        bob_strings = case[2:]
        alice_strings.sort()
        bob_strings.sort()
        if alice_strings[0] < bob_strings[0] and alice_strings[1] < bob_strings[1]:
            print("YES")
        elif alice_strings[0] > bob_strings[0] and alice_strings[1] > bob_strings[1]:
            print("YES")
        else:
            print("NO")