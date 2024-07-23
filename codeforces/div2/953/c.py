t = int(input())

for _ in range(t):
    n_k = list(map(int, input().split()))
    n = n_k[0]
    k = n_k[1]

    a = [i for i in range(1, n+1)]
    a_copy = a.copy()

    if k % 2 == 1:
        print("NO")
        continue

    if n % 2 == 0:
        if k > (n**2)//2:
            print("NO")
            continue
        else:
            current = 0
            while k > 0 and current < n//2:
                val = n-current*2-1
                idx = n//2
                if k == 2 and 2*val != 2:
                    tmp = a[idx]
                    a[idx] = a[idx-1]
                    a[idx-1] = tmp
                    k -= 2
                elif k == 4 and 2*val != 4:
                    tmp1 = a[idx]
                    tmp2 = a[idx+1]
                    a[idx] = a[idx-1]
                    a[idx-1] = tmp1
                    a[idx+1] = a[idx+2]
                    a[idx+2] = tmp2
                    k -= 4
                elif 2*val <= k:
                    tmp = a[current]
                    a[current] = a[n-current-1]
                    a[n-current-1] = tmp
                    k -= 2*val
                current += 1
            print("YES")
            print(" ".join(map(str, a)))
    else:
        if k > ((n-1)*(n+1))//2:
            print("NO")
            continue
        else:
            current = 0
            while k > 0 and current < n//2:
                val = n-current*2-1
                idx = n//2
                if k == 2 and 2*val != 2:
                    tmp = a[idx]
                    a[idx] = a[idx-1]
                    a[idx-1] = tmp
                    k -= 2
                elif k == 4 and 2*val != 4:
                    tmp1 = a[idx]
                    tmp2 = a[idx+1]
                    a[idx] = a[idx-1]
                    a[idx-1] = tmp1
                    a[idx+1] = a[idx+2]
                    a[idx+2] = tmp2
                    k -= 4
                elif 2*val <= k:
                    tmp = a[current]
                    a[current] = a[n-current-1]
                    a[n-current-1] = tmp
                    k -= 2*val
                current += 1
            print("YES")
            print(" ".join(map(str, a)))
