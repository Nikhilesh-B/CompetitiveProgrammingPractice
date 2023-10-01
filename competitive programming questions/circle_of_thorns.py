import math

def sub_segment_area(dir1, dir2, r):
    #dir1 small, #dir2 big
    if dir1 > dir2:
        dir1, dir2 = dir2, dir1
    if dir1>=r and dir2>=r:
        return math.pi*(r**2)*(1/4)
    elif dir1<r and dir2<r and r>=math.sqrt(dir1**2+dir2**2):
        return dir1*dir2
    elif dir1<r and dir2<r and not r>=math.sqrt(dir1**2+dir2**2):
        alpha = math.acos(dir1/r)
        beta = math.acos(dir2/r)
        theta = (math.pi)/2 - alpha - beta
        return 1/2*math.sin(alpha)*dir1*r+1/2*math.sin(beta)*dir2*r+r**2*theta/2
    else:
        return 1/2*(r**2*math.asin(dir1/r)+dir1*math.sqrt(r**2-dir1**2))
         
def compute_expected_value(r, w, h, x, y, v):
    up, down = h-y, y
    right, left = w-x, x
    total_area = 0
    rectangle_area = w*h

    for dir1, dir2 in [(up, right), (right, down), (down, left), (left, up)]:
        sub_segment = sub_segment_area(dir1, dir2, r)
        total_area += sub_segment

    return total_area/rectangle_area*v


if __name__ == "__main__":
    n_r_w_h = input().split(" ")
    n,r,w,h = int(n_r_w_h[0]),int(n_r_w_h[1]),int(n_r_w_h[2]),int(n_r_w_h[3])

    total_value = 0
    for _ in range(n):
        x_y_v = input().split(" ")
        x,y,v = int(x_y_v[0]),int(x_y_v[1]),int(x_y_v[2])
        total_value+=compute_expected_value(r,w,h,x,y,v)

    print(total_value)