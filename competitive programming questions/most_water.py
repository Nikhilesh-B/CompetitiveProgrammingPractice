import math

def most_water(walls):
    m = len(walls)
    lhs = [(walls[0],0) for _ in range(m)]
    rhs = [(walls[len(walls)-1],len(walls)-1) for _ in range(m)]
    for i, h in enumerate(walls):
        if i == 0:
            continue
        if h>lhs[i-1][0]:
            lhs[i] = (h,i)
        else:
            lhs[i] = lhs[i-1]
        
    for j in range(len(walls)-1,-1,-1):
        h = walls[j]
        if j == len(walls)-1:
            continue
        if h>rhs[j+1][0]:
            rhs[j] = (h,j)
        else:
            rhs[j] = rhs[j+1]
    mx_val = -math.inf

    print(lhs, rhs)
    
    for i in range(m):
        hlhs = lhs[i][0]
        hrhs = rhs[i][0]
        h = min(hlhs, hrhs)
        ilhs = lhs[i][1]
        irhs = rhs[i][1]
        w = irhs-ilhs
        mx_val = max(h*w,mx_val)
    
    return mx_val

if __name__ == "__main__":
    walls = [1,30,10,1]
    print(most_water(walls=walls))
