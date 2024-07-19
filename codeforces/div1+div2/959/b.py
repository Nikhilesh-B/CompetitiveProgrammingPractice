t  = int(input())

answers = []
for _ in range(t):
    n = int(input())
    s = input()
    t = input()

    s0 =0
    s1 =0
    t0 =0
    t1 =0

    no_flag = False
    for i in range(n):
        if s[i] == '0':
            s0 += 1
        else:
            s1 += 1
        if t[i] == '0':
            t0 += 1
        else:
            t1 += 1
        
        if t1==1 and s1==0:
            answers.append("NO")
            no_flag = True
            break
        

    if not no_flag:
        answers.append("YES")
    
for answer in answers:
    print(answer)