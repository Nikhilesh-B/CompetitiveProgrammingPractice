t = int(input())
answers = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a_sorted = sorted(a)
    ayes = False
    for i in range(n):
        x = a[0:i]
        y = a[i:]
        if y+x == sorted(y+x):
            ayes = True
            break
    if ayes:
        answers.append('YES')
    else:
        answers.append('NO')

for ans in answers:
    print(ans)
