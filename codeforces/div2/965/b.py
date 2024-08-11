t = int(input())
answers = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    answers.append([a[-1]]+a[0:-1])


for ans in answers:
    print(' '.join(map(str, ans)))