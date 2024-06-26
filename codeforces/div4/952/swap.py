if __name__ == "__main__":
    t = int(input())
    a_s = []
    b_s = []

    for _ in range(t):
        a_b = input().split()
        a_s.append(a_b[0])
        b_s.append(a_b[1])

    for i in range(t):
        a = a_s[i]
        b = b_s[i]
        dummy_a = a[0]
        a = b[0]+a[1:]
        b = dummy_a+b[1:]
        print(a, b)
