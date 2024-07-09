n_k = list(map(int, input().split()))
n = n_k[0]
k = n_k[1]
a = list(map(int, input().split()))

if k >= 3:
    print(max(a))
elif k == 2:
    print(max(a[0], a[-1]))
else:
    print(min(a))
