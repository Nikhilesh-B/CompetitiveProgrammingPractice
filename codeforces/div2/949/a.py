from math import floor, log 

t = int(input())
answers = []    
for _ in range(t):
    l_r = list(map(int, input().split()))
    l = l_r[0]
    r = l_r[1]
    answers.append(floor(log(r,2)))

for answer in answers:
    print(answer)