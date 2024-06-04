if __name__ == "__main__":
    t = int(input())
    n_s = {}
    f_s = {}
    k_s = {}
    a_s = {}

    for i in range(t):
        n, f, k = map(int, input().split())
        n_s[i] = n
        f_s[i] = f
        k_s[i] = k
        a = list(map(int, input().split()))
        a_s[i] = a
    
    for i in range(t):
        n = n_s[i]
        f = f_s[i]
        k = k_s[i]
        a = a_s[i]

        fav_val = a[f-1]

        a.sort(reverse=True)

        split_val = a[k-1]

        if fav_val < split_val:
            print("NO")
        
        elif fav_val > split_val:
            print("YES")
        
        else:
            if k<len(a) and split_val == a[k]:
                print("MAYBE")
            else:
                print("YES")

        

