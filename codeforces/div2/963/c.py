t = int(input())

answers = []
for _ in range(t):
    n_k = list(map(int, input().split()))
    n = n_k[0]
    k = n_k[1]
    a = list(map(int, input().split()))
    a.sort()
    failFlag = False

    mx = a[-1]

    on_int = [mx, mx+k-1]

    for num in a:
        midpoint = mx+(k-((mx-num) % k))-1

        left = ((mx-((mx-num) % k))-1)//k % 1 == 0

        if left:
            if midpoint < on_int[0]:
                failFlag = True
                break
            else:
                on_int[-1] = midpoint

        else:
            if midpoint+1 > on_int[1]:
                failFlag = True
                break
            else:
                on_int[0] = midpoint+1

        if on_int[0] >= on_int[-1]:
            failFlag = True
            break

    if failFlag:
        answers.append(-1)
        continue

    else:
        answers.append(on_int[0])

for ans in answers:
    print(ans)
