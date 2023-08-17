#wrong wrong wrong
def compute_max_sum_adj(adj_arr):
    if len(adj_arr) == 1:
        return adj_arr[0]
    
    ss_exc_key = {0:0}
    max_sum = 0
    for i, num in enumerate(adj_arr):
        if i == 0:
            continue 
        elif i==1:
            print(ss_exc_key, adj_arr)
            ss_exc_key[i] = adj_arr[i-1]
        else:
            ss_exc_key[i] = max(ss_exc_key[i-1], ss_exc_key[i-2]+adj_arr[i-1]) 
        max_sum = max(max_sum, ss_exc_key[i],ss_exc_key[i-1]+num)
    print("keys",ss_exc_key)
    return max_sum

def maxSubsetSum(arr):
    adjacent_positives = []
    pos_in_arow = []
    max_sum = 0
    for i, num in enumerate(arr):
        if num>=0:
            pos_in_arow.append(num)
            if i == len(arr)-1:
                adjacent_positives.append(pos_in_arow)
        else:
            if pos_in_arow:
                adjacent_positives.append(pos_in_arow)
            pos_in_arow = []
    for adj_arr in adjacent_positives:
        max_sum+=compute_max_sum_adj(adj_arr=adj_arr)
    
    return max_sum


if __name__== '__main__':
    arr = [3, 7, 4, 6, 5]
    print(maxSubsetSum(arr))