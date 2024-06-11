def process_case(x,y,z,k):
    smallest = 



if __name__ == "__main__":
    t = int(input())
    x_y_z_k = []
    for _ in range(t):
        x_y_z_k.append(list(map(int, input().split())))

    for i in range(t):
        x, y, z, k = x_y_z_k[i]
        process_case(x, y, z, k)



