import math

def sub_segment_area(dir1, dir2, r):
    #dir1 small, #dir2 big
    if dir1 > dir2:
        dir1, dir2 = dir2, dir1
    
    if dir1>=r and dir2>=r:
        return math.pi*(r**2)*(1/4)
    elif dir1<r and dir2<r and r>math.sqrt(dir1**2+dir2**2):
        return dir1*dir2
    elif dir1<r and dir2<r and not r>math.sqrt(dir1**2+dir2**2):
        theta = (math.pi)/2 - math.acos(dir1/r) - math.acos(dir2/r)
        return dir1*(r/2)+dir2*(r/2)+r**2*theta/2
    else:
    # elif dir2>=r and dir1<r:
        return r*math.sqrt(r**2-dir1**2)/2+(r**2*math.asin(dir1/r))/2
         
def compute_expected_value(r, w, h, x, y, v):
    up, down = h-y, y
    right, left = w-x, x
    print("up",up)
    print("down", down)
    print("right", right)
    print("left", left)
    total_area = 0
    rectangle_area = w*h

    for dir1, dir2 in [(up, right), (right, down), (down, left), (left, up)]:
        total_area += sub_segment_area(dir1, dir2, r)

    if total_area>rectangle_area:
        return v
    
    else:
        return total_area/rectangle_area*v


if __name__ == "__main__":
    print(compute_expected_value(50,100,100,50,90,8))