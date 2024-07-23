t = int(input())
answers = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    rval = a[-1]
    a.pop()
    rval += max(a)

    answers.append(rval)

for answer in answers:
    print(answer)