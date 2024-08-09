t = int(input())

answers = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    o,e=0,0
    lo=-1
    for num in a:
        if num%2==0:
            e+=1
            le=num
        else:
            o+=1
            lo=num

    if o==n or e==n:
        answers.append(0)
        continue
    
    c=0
    # a.reverse()

    # print(a, lo)
    for num in a:
        if num%2==0:
            if num < lo:
                c+=1
                lo=num+lo
            else:
                c+=2
                lo=2*le+lo

    answers.append(c)

for ans in answers:
    print(ans)