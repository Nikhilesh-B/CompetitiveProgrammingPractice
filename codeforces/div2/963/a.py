t = int(input())
answers = []
for _ in range(t):
    n = int(input())
    s = input()
    a,b,c,d = 0,0,0,0

    for char in s:
        if char == "A":
            a+=1
        elif char == "B":
            b+=1
        elif char == "C":
            c+=1
        elif char == "D":
            d+=1
            
    if a>n:
        a=n
    
    if b>n:
        b=n
    
    if c>n:
        c=n

    if d>n:
        d=n
    
    answers.append(a+b+c+d)

for ans in answers:
    print(ans)