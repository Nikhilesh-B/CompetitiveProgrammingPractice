t = int(input())
answers = []
for _ in range(t):
    n = int(input())
    co = n//4
    ch = (n % 4)//2
    answers.append(co+ch)

for ans in answers:
    print(ans)