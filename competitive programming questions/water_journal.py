def compute():
    n_a_b_list = input().split(" ")
    n, mn, mx= int(n_a_b_list[0]),int(n_a_b_list[1]), int(n_a_b_list[2])
    water_logs = []
    for _ in range(n-1):
        water = int(input())
        water_logs.append(water)

    if mn>mx:
        print(-1)   
        return 
    
    mn_seen, mx_seen = False, False
    for wl in water_logs:
        if wl>mx or wl<mn:
            print(-1)
            return
        if wl==mn:
            mn_seen = True  
        if wl==mx:
            mx_seen = True

    if mn == mx:
        print(mx)
        return


    if not mx_seen:
        print(mx)
        return 
    
    if not mn_seen:
        print(mn)
        return
    
    for i in range(mn, mx+1):
        print(i, end=' \n')


if __name__ == "__main__":
    compute()


