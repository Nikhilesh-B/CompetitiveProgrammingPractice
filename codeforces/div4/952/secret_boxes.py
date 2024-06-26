from math import floor
def process_case(x,y,z,k):
    sides = [x, y, z]
    sides.sort()
    min_val = sides[0]
    ratio1 = y/sides[0]
    ratio2 = z/sides[0]

    coefficent = k/(1+ratio1+ratio2)
    #round k down 
    side1 = int(floor(coefficent))
    side2 = int(side1*ratio1)
    side3 = int(side1*ratio2)


    





if __name__ == "__main__":
    t = int(input())
    x_y_z_k = []
    for _ in range(t):
        x_y_z_k.append(list(map(int, input().split())))

    for i in range(t):
        x, y, z, k = x_y_z_k[i]
        process_case(x, y, z, k)



