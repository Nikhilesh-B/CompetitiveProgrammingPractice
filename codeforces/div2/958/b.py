t = int(input())
answers = []


for _ in range(t):
    n = int(input())
    bstr = input()
    blst = [int(x) for x in bstr]

    ocount = 0
    zcount = 0
    zero_segs = 0

    last_was_zero = False

    for i, dig in enumerate(blst):
        if dig == 1:
            ocount += 1
            if last_was_zero:
                last_was_zero = False
        else:
            zcount += 1
            if not last_was_zero:
                zero_segs += 1
                last_was_zero = True

    if ocount > zcount:
        answers.append('YES')

    else:
        if ocount > zero_segs:
            answers.append('YES')
        else:
            answers.append('NO')

for answer in answers:
    print(answer)
