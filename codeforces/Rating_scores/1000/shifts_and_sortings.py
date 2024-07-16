t = int(input())
answers = []

for _ in range(t):
    bstr = input()
    blst = [int(b) for b in bstr]

    one_idx = None
    zero_idx = None
    moves = 0
    for i, b in enumerate(blst):
        if b == 0 and one_idx is not None:
            zero_idx = i

        elif b == 1 and one_idx is None:
            one_idx = i

        if one_idx is not None and zero_idx is not None:
            moves += (zero_idx-one_idx+1)
            one_idx += 1
            zero_idx = None

    answers.append(moves)

for ans in answers:
    print(ans)
